from django.shortcuts import render
from ..models import FinanceData

def finance_chart(request):
    data = FinanceData.objects.all().order_by('year')
    years = [d.year for d in data]
    revenues = [d.revenue for d in data]
    expenditures = [d.expenditure for d in data]

    plot_data = {
        'years': years,
        'revenues': revenues,
        'expenditures': expenditures
    }

    return render(request, 'finance/chart.html', {'plot_data': plot_data})
