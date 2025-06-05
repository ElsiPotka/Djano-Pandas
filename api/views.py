from django.shortcuts import render
from .services import load_sales_data


def sales_data_view(request):
    try:
        df = load_sales_data()

        data_preview = df.head(5).to_html(
            classes="table table-striped", table_id="sales-table"
        )
        columns_list = df.columns.tolist()

        context = {
            "data_preview": data_preview,
            "columns": columns_list,
            "total_rows": len(df),
            "total_columns": len(df.columns),
        }

        return render(request, "api/sales_data.html", context)

    except Exception as e:
        context = {
            "error": str(e),
            "data_preview": None,
            "columns": [],
            "total_rows": 0,
            "total_columns": 0,
        }
        return render(request, "api/sales_data.html", context)
