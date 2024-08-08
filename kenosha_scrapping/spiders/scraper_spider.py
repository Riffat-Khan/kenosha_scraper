import scrapy


class ScraperSpiderSpider(scrapy.Spider):
    name = "scraper_spider"
    allowed_domains = ["www.kenosha.org"]
    start_urls = ["https://www.kenosha.org/building-permit-search"]

    def parse(self, response):
        # Extract the 'Address Range' link
        address_range_link = response.xpath("//li/a[text()='Address Range']/@href").get()
        
        # Check if the link exists and is absolute or relative
        if address_range_link:
            address_range_link = response.urljoin(address_range_link)
            
            # Log the link for debugging
            self.logger.info(f'Found Address Range link: {address_range_link}')
            
            # Follow the link to get the content
            yield scrapy.Request(address_range_link, callback=self.parse_address_range_page)
        else:
            self.logger.info("Address Range link not found.")
            

    def parse_address_range_page(self, response):
        # Extract content from the address range page
        # Adjust the selector based on the actual HTML structure
        content = response.xpath("//div[@class='content-class']//text()").getall()
        
        yield {
            'address_range_content': content
        }
