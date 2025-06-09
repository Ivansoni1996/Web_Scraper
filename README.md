# Web_Scraper
**Theory**
 At its core, web scraping is the automated extraction of data from websites. For news articles, this means programmatically accessing a news website, identifying the relevant parts of an article (headline, author, date, body text, images, etc.), and then saving that information in a structured format.


# Key Concepts
**HTTP Requests**
 How Websites Work: When you type a URL into your browser, your browser sends an HTTP (Hypertext Transfer Protocol) request to the website's server. The server then responds with HTML, CSS, JavaScript, images, etc., which your browser renders as a webpage.

# Scraper's Role
 A web scraper mimics this process. It sends HTTP GET requests to  websites to retrieve the HTML content of a specific   page. Libraries like requests in Python handle this.



# The Foundation
   Web pages are primarily built using HTML . HTML uses tags (e.g., <p>, <h1>, <a>, <div>) to define the structure and content of a page.

# Navigating the Tree
  When the browser receives HTML, it builds a tree-like representation called the DOM. Each HTML element is a node in this tree. Web scrapers parse this HTML to navigate the DOM and locate the specific data they need.

# Identifying Elements
  To extract content, you need to understand how a website structures . This involves inspecting the HTML to find unique identifiers like id attributes, class attributes, or specific tag hierarchies that consistently contain the desired information.

# Parsing HTML
  **Making Sense of Markup** 
  Raw HTML is a string of text. To extract data, you need a parser that can understand the HTML structure and allow you to navigate it.

# Selectors
   Parsers use various methods to select specific elements

# Tag Name  
   Select all <p> tags.

# CSS Selectors
   Similar to how CSS styles elements (e.g., .headline, #article-body, div.content p). These are powerful and widely used.

# Data Extraction 

  Once you've selected an element, you extract its content. This could be:
  Text Content: The visible text within a tag (e.g., the text inside a <p> tag).
  Attribute Values: The value of an attribute (e.g., the href attribute of an <a> tag for a link, or the src attribute of an <img> tag for an image URL).

# Data Storage

 After extraction, you need to store the data in a structured format. Common choices include csv,json,md,txt

# Ethical and Legal Considerations

  Before i even start coding, this has to be considered:

# Robots.txt

  This file (e.g., https://example.com/robots.txt) is a standard for websites to communicate with web crawlers/scrapers. It specifies which parts of the site should not be crawled. Always check and respect robots.txt. Ignoring it can lead to your IP being blocked or legal issues.

# Terms of Service
  Many websites explicitly prohibit scraping in their terms of service. Read Tos of the website you intend to scrape. Violating ToS can lead to legal action.

# Copyright

  The content you scrape  is copyrighted. You cannot republish copyrighted material without permission. Scraping is generally for personal research, analysis, or internal use, not for redistribution.

# Rate Limiting and IP Blocking

  Scraping too aggressively can overload a website's server. Websites often implement rate limiting (restricting the number of requests from an IP in a given time) and IP blocking to prevent this.
  Be courteous: Introduce delays between requests (time.sleep()), use proxies, and rotate user agents to avoid detection and being blocked.

# Dynamic Content (JavaScript-rendered pages)

  Many modern websites use JavaScript to load content asynchronously after the initial HTML is loaded. Simple requests libraries won't execute JavaScript.

# Identify APIs
  Sometimes the data is loaded from a public API that you can directly access.
  Headless Browsers: Tools like Selenium or Playwright can control a real browser (without a visible GUI) to execute JavaScript and render the page before scraping. This is more resource-intensive but necessary for dynamic content.