def returns_sheet(soup, work_sheet):
    from datetime import datetime
    items = soup.find_all(class_='serp-item')
    for i in items:
        name = i.find(class_='serp-item__title').text
        url = i.find(class_='bloko-link').attrs['href']
        price = i.find(attrs={'data-qa': 'vacancy-serp__vacancy-compensation'})
        date = datetime.now()
        if price is not None:
            price = price.text.replace('EUR', '€')
            price = price.replace('USD', '$')
            price = price.replace('руб.', '₽')
            price = ''.join([i for i in price if i.isdigit() or (i in ['–', '€', '$', '₽'])])
        else:
            price = 'не указано'
        row = [name, url, price, date]
        work_sheet.append(row)
    return work_sheet

