from bs4 import BeautifulSoup

with open('home.html', 'r') as html_file:
    content = html_file.read()
    # print(content)
    
    soup = BeautifulSoup(content, 'lxml')
    # print(soup.prettify())
    
    courses_html_tags = soup.find_all('h5')
    print(courses_html_tags)
    
    for course in courses_html_tags:
        print(course.text)
        
    prices_html_tags = soup.find_all('a')
    # print(prices_html_tags)
    
    for price in prices_html_tags:
        print(price.text)
        
    print("\n")
    
    course_cards = soup.find_all('div', class_='course')
    
    for course in course_cards:
        course_name = course.find('h5').text
        course_price = course.find('a').text
        print(f"Course: {course_name}, Price: {course_price}")
    