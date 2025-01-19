# LinkedIn IIT Graduate Profile Scraper & Analyzer

## Project Structure

```
/task_2/
├── linkedin_scraper.py    # Main scraping implementation
├── iit_alumni_data.csv    # Output data file
└── README.md             # Documentation
```

## Core Components

### 1. Profile Scraper (`LinkedInProfileCrawler` class)
- Automated LinkedIn login
- Profile data extraction
- Configurable search functionality
- Rate limiting protection

### 2. Data Collection
```python
crawler = LinkedInProfileCrawler(
    email='your_linkedin_connected_mail',
    password='its_passsword'
)

# Profile URLs to scrape
iit_profiles = [
    "https://www.linkedin.com/in/example1/",
    "https://www.linkedin.com/in/example2/"
]
```

### 3. Data Fields Collected
- Name
- Job Title
- Company
- Location (from search results)
- Profile URL

## Usage Guide

1. **Setup Requirements**
```bash
pip install selenium pandas matplotlib seaborn
```

2. **Configuration**
- Update email/password in main()
- Add target profile URLs to iit_profiles list
- Adjust delays if needed (default: 3-7 seconds)

3. **Run Scraper**
```bash
python linkedin_scraper.py
```

## Output Format

### CSV Structure
```csv
name,job_title,company
John Doe,Software Engineer,Google
Jane Smith,Data Scientist,Microsoft
```

## Safety Features

1. **Rate Limiting Protection**
- Random delays between requests
- Progressive page scrolling
- Error handling for failed requests

2. **Data Validation**
- URL format verification
- Fallback to URL-derived names
- Missing data handling

## Best Practices

1. **Ethical Scraping**
- Respect LinkedIn's terms of service
- Use reasonable delays between requests
- Only collect publicly available data

2. **Error Handling**
- Graceful failure handling
- Comprehensive error logging
- Session management

## Security Notes

- Store credentials securely
- Don't commit credentials to version control
- Use environment variables for sensitive data

## Data Processing Tips

1. **Standardization**
```python
# Example data cleaning
data['company'] = data['company'].str.strip().str.title()
data['job_title'] = data['job_title'].str.strip().str.lower()
```

2. **Analysis Preparation**
```python
# Group by company
company_stats = data.groupby('company').size()

# Role analysis
role_distribution = data['job_title'].value_counts()
```

## Limitations

- Requires LinkedIn account
- Subject to LinkedIn's rate limits
- Limited to public profile data
- HTML structure dependent

## Contributing

1. Fork the repository
2. Create a feature branch
3. Submit a pull request