# Dogana e Kosovës

**Dogana e Kosovës** is a data analysis and visualization project that focuses on analyzing open data related to Kosovo's trade balance and economic activities. The project explores patterns and trends over the year, offering a comprehensive look at the annual developments in Kosovo's trade sector. Through advanced data analysis techniques and visualizations, it provides clear insights into how trade balances evolve over time and the factors influencing these changes.

This project contains detailed analyses and visualizations, including revenue generated by year, excise taxes by month, the value of prohibited goods, and top import sources by quantity. It also presents charts for customs taxes, VAT (TVSH), and excise taxes, alongside percentage-based trends for goods value, net weights, and total tax collections across various charts. These insights offer valuable perspectives for understanding Kosovo’s trade and customs activities.

## Built With

This data analysis and visualization project was developed using the following tools, technology, and resources:
- **Python**
- **Microsoft Word**
- **Microsoft Excel**
- **Kosovo Customs Open Data Import** — [Reference link](https://dogana.rks-gov.net/OpenData/Index?id=4)

## Features

✅ **Data Import and Preparation:** Reads data files, processes them for analysis, and converts strings to numeric formats for accurate computations.

✅ **Comprehensive Trade Data Analysis:** Analyzes customs statistical data, including trade balances, revenue streams, and unique product imports.

✅ **Yearly and Monthly Revenue Trends:** Tracks the total amount of revenue generated by year, including detailed breakdowns of excise tax by year and month.

✅ **Customs and Tax Visualizations:** Creates charts showcasing trends in customs taxes, excise taxes, and VAT (TVSH) taxes, along with combined tax presentations.

✅ **Prohibited Goods and Net Weights:** Examines the total value of prohibited goods and computes average values for net weights of imports.

✅ **Country-Based Analysis:** Identifies top import countries by quantity and groups imports by country for comparative insights.

✅ **Percentage-Based Insights:** Provides percentage trends for VAT (TVSH) tax collection, total taxes, goods value, and net weight, including quarterly breakdowns.

## Prerequisites

Before starting, ensure the following are installed on your system:
- **Python**
  - Download the [Python Installer](https://www.python.org/downloads/).
  - Follow the [installation guide](https://docs.python.org/3/using/index.html) to install and configure it properly.
  - Verify your Python installation by running the following command in your terminal:
    ```
    python --version
    ```
  - Ensure your system's `PATH` is properly configured to allow Python commands to run globally from any location.
- **Microsoft Office**
  - Download the [Microsoft Office](https://www.microsoft.com/en-us/download/office).
  - Follow the [installation guide](https://support.microsoft.com/en-us/office/download-install-or-reinstall-microsoft-365-office-2024-or-office-2021-on-a-pc-or-mac-4414eaaf-0478-48be-9c42-23adc4716658) to install and set it up correctly.
  - An active Microsoft 365 subscription or a standalone Office license is required.

## Installation

1. Clone or download the repository to your local machine:
   ```
   git clone https://github.com/ndriqimlahu/dogana-kosoves.git
   ```
2. Open the repository folder in your preferred IDE or code editor.
3. Navigate to the `Source` directory and locate the `DataAnalysis.py` and `DataVisualization.py` files.
4. Run the application using your IDE's built-in tools or code editor extensions.

## Screenshots

Below you can see some additional useful screenshots of what the data analysis and visualization project looks like and how it can be used:

- Reading CSV file from Kosovo Customs | Total amount of quantity (incomes) generated by year
<div>
   <img src="https://raw.githubusercontent.com/ndriqimlahu/dogana-kosoves/main/Preview/01-Leximi%20i%20fajllit%20nga%20Dogana%20e%20Kosoves.png" align="top" width="48%" height="auto">
   <img src="https://raw.githubusercontent.com/ndriqimlahu/dogana-kosoves/main/Preview/02-Shuma%20e%20sasise%20(te%20hyrave)%20te%20realizura%20sipas%20vitit.png" align="top" width="48%" height="auto">
   <hr>
</div>

- Total amount of excise tax by year and month | Total value of goods prohibited by customs
<div>
   <img src="https://raw.githubusercontent.com/ndriqimlahu/dogana-kosoves/main/Preview/03-Shuma%20e%20taks%C3%ABs%20s%C3%AB%20akciz%C3%ABs%20sipas%20vitit%20dhe%20muajit.png" align="top" width="48%" height="auto">
   <img src="https://raw.githubusercontent.com/ndriqimlahu/dogana-kosoves/main/Preview/04-Shuma%20e%20vlerave%20t%C3%AB%20mall%C3%ABrave%20t%C3%AB%20ndaluara%20nga%20Dogana.png" align="top" width="48%" height="auto">
   <hr>
</div>

- Average value for net weights | Imports or revenues of unique products from customs
<div>
   <img src="https://raw.githubusercontent.com/ndriqimlahu/dogana-kosoves/main/Preview/05-Vlera%20mesatare%20p%C3%ABr%20peshat%20neto.png" align="top" width="48%" height="auto">
   <img src="https://raw.githubusercontent.com/ndriqimlahu/dogana-kosoves/main/Preview/06-Importet%20apo%20t%C3%AB%20hyrat%20e%20produkteve%20unike%20nga%20Dogana.png" align="top" width="48%" height="auto">
   <hr>
</div>

- Top countries from which imports are made in quantity | Deleting some specified columns
<div>
   <img src="https://raw.githubusercontent.com/ndriqimlahu/dogana-kosoves/main/Preview/07-Top%20shtetet%20nga%20t%C3%AB%20cilat%20b%C3%ABhet%20importi%20me%20sasi.png" align="top" width="48%" height="auto">
   <img src="https://raw.githubusercontent.com/ndriqimlahu/dogana-kosoves/main/Preview/08-Fshirja%20e%20disa%20kolonave%20t%C3%AB%20caktuara.png" align="top" width="48%" height="auto">
   <hr>
</div>

- Grouping by country, collecting and sorting by customs tax | Chart according to customs tax, excise tax and VAT (TVSH) tax
<div>
   <img src="https://raw.githubusercontent.com/ndriqimlahu/dogana-kosoves/main/Preview/09-Grupimi%20sipas%20shteteve%2C%20mbledhja%20dhe%20sortimi%20sipas%20taks%C3%ABs%20s%C3%AB%20dogan%C3%ABs.png" align="top" width="48%" height="auto">
   <img src="https://raw.githubusercontent.com/ndriqimlahu/dogana-kosoves/main/Preview/10-Grafiku%20sipas%20taks%C3%ABs%20s%C3%AB%20dogan%C3%ABs%2C%20akciz%C3%ABs%20dhe%20tvsh-s%C3%AB.png" align="top" width="48%" height="auto">
   <hr>
</div>

- Chart by quantity, value of goods and net weight | Percentage of VAT (TVSH) tax collected by months of the year
<div>
   <img src="https://raw.githubusercontent.com/ndriqimlahu/dogana-kosoves/main/Preview/11-Grafiku%20sipas%20sasis%C3%AB%2C%20vler%C3%ABs%20s%C3%AB%20mallrave%20dhe%20pesh%C3%ABs%20neto.png" align="top" width="48%" height="auto">
   <img src="https://raw.githubusercontent.com/ndriqimlahu/dogana-kosoves/main/Preview/12-P%C3%ABrqindja%20nga%20taksa%20tvsh-s%C3%AB%20e%20grumbulluar%20sipas%20muajve%20t%C3%AB%20vitit.png" align="top" width="48%" height="auto">
   <hr>
</div>

- Percentage of taxes and value of goods in total | Percentage of goods value and net weight in total for the first 4 months of the year
<div>
   <img src="https://raw.githubusercontent.com/ndriqimlahu/dogana-kosoves/main/Preview/13-P%C3%ABrqindja%20e%20taksave%20dhe%20vler%C3%ABs%20s%C3%AB%20mallrave%20n%C3%AB%20total.png" align="top" width="48%" height="auto">
   <img src="https://raw.githubusercontent.com/ndriqimlahu/dogana-kosoves/main/Preview/14-P%C3%ABrqindja%20e%20vler%C3%ABs%20s%C3%AB%20mallrave%20dhe%20pesh%C3%ABs%20neto%20n%C3%AB%20total%20p%C3%ABr%204%20mujorin%20e%20vitit%202021.png" align="top" width="48%" height="auto">
   <hr>
</div>

- Presentation of the customs tax chart | Presentation of the excise tax chart
<div>
   <img src="https://raw.githubusercontent.com/ndriqimlahu/dogana-kosoves/main/Preview/15.1-Paraqitja%20e%203%20grafeve%20p%C3%ABr%20taksat%20n%C3%AB%20nj%C3%AB%20figur%C3%AB.png" align="top" width="48%" height="auto">
   <img src="https://raw.githubusercontent.com/ndriqimlahu/dogana-kosoves/main/Preview/15.2-Paraqitja%20e%203%20grafeve%20p%C3%ABr%20taksat%20n%C3%AB%20nj%C3%AB%20figur%C3%AB.png" align="top" width="48%" height="auto">
   <hr>
</div>

- Presentation of the VAT (TVSH) tax chart | Presentation of all taxes in one chart
<div>
   <img src="https://raw.githubusercontent.com/ndriqimlahu/dogana-kosoves/main/Preview/15.3-Paraqitja%20e%203%20grafeve%20p%C3%ABr%20taksat%20n%C3%AB%20nj%C3%AB%20figur%C3%AB.png" align="top" width="48%" height="auto">
   <img src="https://raw.githubusercontent.com/ndriqimlahu/dogana-kosoves/main/Preview/16-Paraqitja%20e%20taksave%20n%C3%AB%20nj%C3%AB%20grafik%20t%C3%AB%20vet%C3%ABm.png" align="top" width="48%" height="auto">
</div>

## Support

If you find this project useful, please consider giving it a star!
