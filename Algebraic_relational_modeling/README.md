# Database Exercise 5
## Algrebaic relational modeling

###### SETUP:
- `docker pull jegp/soft2018-data `<br>
- `docker pull jegp/soft2018-jupyter`<br>
- `docker run -p 5432:5432 --name data -d jegp/soft2018-data`<br>
- `docker exec -it data bash -c "psql -U appdev"`<br>
- `docker run -p 8888:8888 --name jupyter --link data -it jegp/soft2018-jupyter`
  or <br>
`docker run -p 8888:8888 -v /vagrant/jupyter:/home/jovyan --name jupyter --link data -it jegp/soft2018-jupyter `<br>
- use the generated token as the login


###### SETUP for running SQL commands using jupyter notebook:

```python
%load_ext sql
```


```python
%sql postgresql://appdev@data:5432/appdev
```




    'Connected: appdev@appdev'

