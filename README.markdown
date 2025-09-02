# News Aggregator

A Python-based news aggregator that collects articles from various RSS feeds, processes them, and stores them in a PostgreSQL database. The project fetches news data from multiple sources and categories, such as Top Stories, Tech, Sports, Health, Politics, Entertainment, India, and World news, and organizes it for easy access.

## Features
- Fetches news articles from RSS feeds of popular sources like Times of India, NDTV, The Hindu, and more.
- Extracts article titles, descriptions, links, and publication dates.
- Stores the collected data in a PostgreSQL database.
- Supports multiple news categories (e.g., Tech, Sports, Politics).
- Handles errors gracefully during data collection and storage.

## Prerequisites
To run this project, ensure you have the following installed:
- Python 3.8+
- PostgreSQL (with a database named `newsag`)
- Required Python libraries: `psycopg2`, `requests`, `beautifulsoup4`

## Installation
1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/news-aggregator.git
   cd news-aggregator
   ```

2. **Install dependencies**:
   ```bash
   pip install psycopg2-binary requests beautifulsoup4
   ```

3. **Set up PostgreSQL**:
   - Ensure PostgreSQL is installed and running.
   - Create a database named `newsag`:
     ```sql
     CREATE DATABASE newsag;
     ```
   - Update the database connection details in `SQlQuerries.py` (e.g., `host`, `port`, `user`, `password`) to match your PostgreSQL setup.

4. **Prepare the RSS feeds file**:
   - The `RSS-Feeds` file contains a list of RSS feed URLs, categorized by topic and source (e.g., `Top Stories, times of india, http://timesofindia.indiatimes.com/rssfeedstopstories.cms`).
   - Ensure this file is in the project directory and formatted correctly (category, source, URL separated by commas).

## Usage
1. **Run the news aggregator**:
   ```bash
   python linkTraverser.py
   ```
   This script:
   - Reads RSS feed URLs from the `RSS-Feeds` file.
   - Fetches articles using the `DataCollector` class.
   - Stores the data in the PostgreSQL database using `SQlQuerries`.
   - Prints the fetched titles, descriptions, and links for verification.

2. **Database Structure**:
   The project creates a table named `NewsArticles` with the following schema:
   - `id`: Auto-incremented primary key
   - `Title`: Article title (VARCHAR)
   - `Description`: Article summary (TEXT)
   - `Source`: News source (VARCHAR)
   - `Catagory`: News category (VARCHAR)
   - `Link`: URL to the full article (TEXT)

3. **Example Output**:
   When you run `linkTraverser.py`, it will:
   - Fetch articles from each RSS feed.
   - Store them in the `NewsArticles` table.
   - Display the titles, descriptions, and links for each feed, along with a confirmation of how many articles were inserted.

## Project Structure
- `SQlQuerries.py`: Handles PostgreSQL database connection and stores news articles.
- `dataCollector.py`: Fetches and parses RSS feed data using `requests` and `BeautifulSoup`.
- `linkTraverser.py`: Traverses the RSS feed URLs, collects data, and stores it in the database.
- `RSS-Feeds`: A text file listing RSS feed URLs, categorized by topic and source.

## Contributing
Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a new branch (`git checkout -b feature/your-feature`).
3. Make your changes and commit (`git commit -m 'Add your feature'`).
4. Push to the branch (`git push origin feature/your-feature`).
5. Open a pull request.

## License
This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgments
- Built with [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) for XML and HTML parsing.
- Uses [psycopg2](https://www.psycopg.org/) for PostgreSQL integration.
- Inspired by the need for a centralized news aggregation system.

## Contact
For questions or suggestions, feel free to open an issue on GitHub or contact [burhanuddintelwala75@gmail.com](mailto:burhanuddintelwala75@gmail.com).
