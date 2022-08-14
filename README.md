# l33t.ltd python api wrapper

## Description
Python 2/3 library for the [anti-captcha](https://l33t.ltd) web site

### Getting APi key
Register at [l33t website](https://l33t.ltd). Go to the main page and click Profile. Follow "Infromation" tab. Here you can see your API key and balance in rubles(₽)
![image](https://user-images.githubusercontent.com/58441229/184551118-c0101678-449d-44c9-882b-d12bb2f652d0.png)



## Functions
- get balance
- get threads
- get free theads
- solve REcaptcha
- solve image captcha

# Examples
## Get balance
```python
import lib

solver = ApiWrapper("your-api-key")
print(solver.get_balance())
```

## Get using api key

```python
import lib

solver = ApiWrapper("your-api-key")
print(solver.get_key())
```

## Updating key
```python
import lib

solver = ApiWrapper("your-api-key-1")
solver.update_key("your-api-key2")
```

## Get all threads & free threads
```python
import lib

solver = ApiWrapper("your-api-key")
all_threads = solver.get_threads()
free_threads = solver.get_free_threads()
pinr(f"{all_threads} threads are possible and {free_threads} are free")
```

## Send REcapthca v2 to server

```python
import lib

solver = ApiWrapper("your-api-key")
cap_data = solver.solve_recaptcha(cap_version=2, sitekey="6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-",
                                  is_json=1, page_url="https://www.google.com/recaptcha/api2/demo")
captcha_id = cap_data["request"]
```

## Send REcapthca v3 to server

```python
import lib

solver = ApiWrapper("your-api-key")
cap_data = solver.solve_recaptcha(cap_version=3, k_value="6LfwIo4UAAAAADauXCK0Ke_jIWNSW-z49N-IUj43",
                                  is_json=1, page_url="https://demo.codeforgeek.com/recaptcha-v3/")
captcha_id = cap_data["request"]
```

## Sending image captcha to server
import lib

solver = ApiWrapper("your-api-key")
cap_data = solver.solve_imgcaptcha(captcha_str="long_base64_string_of_captcha", is_json=1)
captcha_id = cap_data["request"]
```

## Get captcha answer
```python
import lib

solver = ApiWrapper("your-api-key")
print(solver.get_cap_answer(cap_id=326119, is_json=1))  # cap_id is captcha_id from the previous exmaples
```
