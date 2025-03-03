# Parser API

Варианты использования api:
- Очистка таблицы в базе данных
```
curl "http://89.31.116.38:5000/api/clear"
```
- Получение json результата парсинга:
```
curl "http://89.31.116.38:5000/api/data"
``` 
- Вызов работы парсера:
Аргументы:
1) `product` - продукт, карточки которого необходимо распарсить (по умолчанию 'стрелы для лука')
2) `pages_count` - количество страниц для парсинга (по умолчанию 2)
```
curl "http://89.31.116.38:5000/api/parser"
curl "http://89.31.116.38:5000/api/parser?product='pencil'"
curl "http://89.31.116.38:5000/api/parser?pages_count=5"
curl "http://89.31.116.38:5000/api/parser?product='pencil'&pages_count=5"
``` 
