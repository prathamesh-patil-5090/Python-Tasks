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


# Career Path Analysis for IIT Graduates

## Data Analysis Approach

### 1. Career Trajectory Analysis
```python
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def analyze_career_patterns(csv_file):
    df = pd.read_csv(csv_file)
    
    # Company tier classification
    company_tiers = {
        'FAANG': ['Google', 'Facebook', 'Amazon', 'Apple', 'Netflix'],
        'Startups': ['startup', 'founder', 'co-founder'],
        'MNC': ['Microsoft', 'IBM', 'Oracle', 'Intel']
    }
    
    # Role classification
    role_categories = {
        'Technical': ['engineer', 'developer', 'architect'],
        'Management': ['manager', 'director', 'head'],
        'Research': ['scientist', 'researcher', 'PhD']
    }
    
    return {
        'company_distribution': analyze_companies(df),
        'role_progression': analyze_roles(df),
        'industry_trends': analyze_industries(df)
    }
```

### 2. Key Analysis Areas

1. **Initial Career Choices**
- First job selection
- Starting role distribution
- Geographic preferences
```python
def analyze_initial_roles(df):
    entry_roles = df['job_title'].value_counts()
    return {
        'most_common': entry_roles.head(),
        'technical_ratio': calculate_technical_ratio(entry_roles),
        'location_preference': df['location'].value_counts()
    }
```

2. **Career Progression Patterns**
- Technical to Management transitions
- Industry switching frequency
- Startup vs Corporate paths
```python
def analyze_progression(df):
    return {
        'tech_to_management': track_role_transitions(df),
        'industry_changes': analyze_industry_moves(df),
        'startup_ratio': calculate_startup_involvement(df)
    }
```

3. **Success Indicators**
- Time to leadership roles
- Company tier progression
- International career moves

### 3. Visualization Strategy

1. **Career Flow Analysis**
```python
def visualize_career_flows(df):
    # Sankey diagram for career transitions
    plt.figure(figsize=(12, 8))
    create_career_flow_diagram(df)
    plt.title('IIT Graduate Career Transitions')
    plt.savefig('career_flows.png')
```

2. **Industry Distribution**
```python
def plot_industry_trends(df):
    # Pie chart of industry distribution
    industry_dist = df['company'].value_counts()
    plt.figure(figsize=(10, 10))
    plt.pie(industry_dist.values, labels=industry_dist.index)
    plt.title('Industry Distribution')
    plt.savefig('industry_distribution.png')
```

## Insights Generation

### 1. Quantitative Metrics
- Average time in first role
- Percentage in technical vs management
- Startup founding rate
- International placement rate

### 2. Trend Analysis
- Popular career transitions
- Emerging industry preferences
- Geographic movement patterns
- Salary progression (if available)

### 3. Pattern Recognition
- Common success paths
- Industry-specific progressions
- Role transition triggers
- Education impact (higher studies)

## Implementation Example

```python
def generate_insights_report(csv_file):
    df = pd.read_csv(csv_file)
    
    insights = {
        'career_starts': analyze_initial_roles(df),
        'progression': analyze_progression(df),
        'patterns': identify_patterns(df)
    }
    
    # Generate visualizations
    create_visualizations(df)
    
    # Create report
    with open('career_insights.md', 'w') as f:
        f.write(format_insights(insights))
    
    return insights
```

## Recommendations for Future Analysis

1. **Data Enhancement**
   - Include education details
   - Add timeline information
   - Track salary ranges
   - Note industry categories

2. **Advanced Analytics**
   - Machine learning for pattern detection
   - Predictive career modeling
   - Network effect analysis
   - Success factor correlation

3. **Interactive Visualization**
   - Dynamic career path flows
   - Interactive dashboards
   - Time-based animations
   - Comparative analysis tools
