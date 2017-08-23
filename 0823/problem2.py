# #### 2.包包問題：一個最大能容納50公斤的包包，現在一共有三樣價值與重量不同的東西要放入其中，請問放置後的最大價值為多少？ 

# In[25]:

def find_optinal_value(capacity,values,weights):
    value = 0
    valuePerWeight = sorted([[values/weights,weights] for values,weights in zip(values,weights) ],reverse=True)

    while capacity >0 and valuePerWeight:
        maxi = 0
        idx = None
        for i,item in enumerate(valuePerWeight):        
            if item[1]>0 and item[0]>maxi:
                maxi = item[0]
                idx = i
                
        if idx is None:
            return 0.
        
        w = valuePerWeight[idx][1]
        v_per = valuePerWeight[idx][0]
    
        if w >= capacity:
            value += v_per*capacity
            capacity = 0
            return value
    
        else:
            value += v_per*w
            capacity -= w
    
        valuePerWeight.pop(idx)
            