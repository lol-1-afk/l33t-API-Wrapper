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

solver = ApiWrapper("84676dcbe7db732fea47251c7750ecdf")
print(solver.get_balance())
```
