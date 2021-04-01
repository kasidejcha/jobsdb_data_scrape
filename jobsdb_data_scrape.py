from bs4 import BeautifulSoup
import requests

def run_jobsdb_scape():

    url1 = 'https://th.jobsdb.com/th/data-scientist-jobs-in-bangkok/1?Key=data'
    url2 = 'https://th.jobsdb.com/th/data-scientist-jobs-in-bangkok/2?Key=data'
    url3 = 'https://th.jobsdb.com/th/data-scientist-jobs-in-bangkok/3?Key=data'
    url=[url1, url2, url3]
    page_num = int(input('Scrape Page Number(1-3): '))
    url=url[page_num-1]
    
    html_text = requests.get(url).text
    soup = BeautifulSoup(html_text, 'html.parser')

    raw_filter_position = input('Filter unwanted position: ')
    filter_position = raw_filter_position.split(', ')
    print(f'Filtering out: {filter_position}')
    print('')

    def converttostr(input_seq, seperator):
        # Join all the strings in list
        final_str = seperator.join(input_seq)
        return final_str

    jobs = soup.find_all('div', class_='FYwKg _20Cd9_0 _1GAuD _3MPd_ _3ftyQ _1lyEa')

    for job in jobs:
        position = job.find('div', class_='FYwKg _2j8fZ_0 sIMFL_0 _1JtWu_0').text
        position = position.split(' ')
        result = any(element in position for element in filter_position)
        if result == False:
            company_name = job.find('span', class_='FYwKg _2Bz3E C6ZIU_0 _6ufcS_0 _2DNlq_0 _29m7__0').text
            requirement = job.find_all('span', class_="FYwKg _2Bz3E C6ZIU_0 _1_nER_0 _2DNlq_0 _29m7__0 _1PM5y_0")
            Location = job.find('span', class_="FYwKg _3MPd_ _2Bz3E And8z").text
            Link = 'https://th.jobsdb.com' + job.find('div',class_='FYwKg').h1.a['href']
            time = job.find('time', class_="FYwKg _2Bz3E")['datetime']

            #print(job)
            print(f'Company Name: {company_name}')
            print(f"position: {converttostr(position, ' ')}")
            print(f'Location: {Location}')
            if len(requirement) == 3:
                print('Requirement:')
                print('• ',requirement[0].text)
                print('• ',requirement[1].text)
                print('• ',requirement[2].text)
            else:
                print('Requirement not found')
            print('Link: ', Link)
            print('Date Posted: ', time[:10])
            print('')
            print('')
