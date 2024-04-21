from django.shortcuts import render
import json
from ..models import FinanceData

def finance_chart(request):
    data = FinanceData.objects.all().order_by('year')
    years = [d.year for d in data]
    revenues = [d.revenue for d in data]
    expenditures = [d.expenditure for d in data]

    plot_data = {
        "years": years,
        "revenues": revenues,
        "expenditures": expenditures
    }

    print(plot_data)
    print("#################")

    # plot_dataをJSON文字列に変換
    plot_data_json = json.dumps(plot_data)

    print(plot_data_json)

    return render(request, 'chart.html', {'plot_data': plot_data_json})
