# My simple API

## Requirements:
* docker >= 24
* docker-compose

## Quick Start
1. Clone this repository:  
```
git clone https://github.com/Aleksandr-Mamonov/my_simple_api.git
```
2. Change directory:  
```
cd my_simple_api
```
3. Run docker-compose:  
```
docker-compose up -d
```
4. After all containers are up and running, try out API:  
    4.1 Create key:value pair and store it in DB:  
   
    ```
    curl -H "Content-Type: application/json" -X POST -d '{"some_key":"some_value"}' http://127.0.0.1:8080/add
    ```
    4.2 Update existing key pair witn new value:  
    ```
    curl -H "Content-Type: application/json" -X PUT -d '{"some_key":"new_value"}' http://127.0.0.1:8080/update
    ```
    4.3 Read key:value pair from db by providing query parameter `key` in URL:
    ```
    http://127.0.0.1:8080/get?key=some_key
    ```

To stop docker-compose:
```
docker-compose down
```
