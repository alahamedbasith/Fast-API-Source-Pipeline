from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import pandas as pd
from typing import List

app = FastAPI()

# Load the Excel file and convert it to a pandas DataFrame
df = pd.read_excel("SaleData.xlsx")


@app.get("/")
async def read_root() -> List[str]:
    return ["Working Good"]

@app.get("/data", response_model=List[dict])
async def read_data():
    return [
        {"id": 1, "name": "Ahamed Basith"}, 
        {"id": 2, "name": "Jane Doe"},
        {"id": 3, "name": "Najim"},

        ]

# New endpoint to return the whole records as an HTML table
@app.get("/all_data", response_class=HTMLResponse)
async def get_all_data():
    # Convert the DataFrame to HTML
    html_data = df.to_html(classes='table table-striped', index=False)

    # Return the HTML content
    return f"""
    <html>
        <head>
            <title>Sale Data</title>
            <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css">
        </head>
        <body>
            <div class="container">
                <h2>Sale Data</h2>
                {html_data}
            </div>
        </body>
    </html>
    """

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=5000)
