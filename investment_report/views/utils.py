import csv

from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, StreamingHttpResponse
from django.utils import translation
from django.conf import settings
from django.contrib.auth.decorators import login_required


from investment_report.utils import (
    investment_report_html_generator, investment_report_pdf_generator
)

from investment_report.models import Market, Sector, PIRRequest


@login_required
def investment_report_html(request, lang, market, sector, moderated=True):
    """
    Used for previewing on dev
    """
    market = get_object_or_404(Market, name=market)
    sector = get_object_or_404(Sector, name=sector)
    company = request.GET.get('company', 'You')
    lang = request.GET.get('lang', settings.LANGUAGE_CODE)

    with translation.override(lang):
        return HttpResponse(
            str(investment_report_html_generator(
                market, sector, company, local=False, moderated=moderated
            )[0])
        )


@login_required
def investment_report_pdf(request, lang, market, sector, moderated=True):
    """
    Used for previewing on the admin
    """
    market = get_object_or_404(Market, name=market)
    sector = get_object_or_404(Sector, name=sector)
    company = request.GET.get('company', 'You')
    translation.activate(lang)

    with translation.override(lang):
        pdf_file = investment_report_pdf_generator(
            market, sector, company, local=True, moderated=moderated
        )

        pdf = pdf_file.getvalue()
        pdf_file.close()

        response = HttpResponse(content_type='application/pdf')
        response.write(pdf)
        return response


class Echo:
    """An object that implements just the write method of the file-like
    interface.
    """
    def write(self, value):
        """Write the value by returning it, instead of storing in a buffer."""
        return value


@login_required
def pir_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="pir_reports_export.csv"'

    fields = [
        'id', 'country', 'market__name', 'sector__name', 'name',
        'lang', 'company', 'email', 'date_created',
    ]

    writer = csv.DictWriter(
        response,
        fieldnames=fields
    )

    writer.writeheader()

    for p in PIRRequest.objects.order_by('id').values(*fields):
        writer.writerow(p)

    return response