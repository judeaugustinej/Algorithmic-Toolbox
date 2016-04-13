# Uses python3
import sys

def get_optimal_value(capacity, weights, wvalues):

    value = 0.
    #more time
    
    cost_list = list()
    for wvalue, weight in zip(wvalues, weights):
        cost_list.append([(wvalue / weight), weight])
    #print(cost_list)
    sorted_list = sorted(cost_list)
    #print(sorted_list)
    
    while sorted_list and capacity>0:
        largest_weight = sorted_list[-1][1]
        largest_val = sorted_list[-1][0]
        #print(largest_weight, largest_val,capacity)
        if largest_weight <= capacity:
            value = value + (largest_val * largest_weight)
        else:
            value = value + (largest_val * capacity)
        capacity = capacity - largest_weight
        sorted_list.pop()
        #print(value, capacity, sorted_list)
    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
    """
    # Uses python3
    import sys

    def get_optimal_value(capacity, weights, wvalues):

        value = 0.
  
        cost_dict = dict()
        for wvalue, weight in zip(wvalues, weights):
            cost_dict[weight] = (wvalue / weight)
        while capacity>0:
            if cost_dict:
                largest_key = max(cost_dict, key=cost_dict.get)
                largest_val = cost_dict[largest_key]
                if largest_key <= capacity:
                    value = value + (largest_val * largest_key)
                    capacity = capacity - largest_key
                    del cost_dict[largest_key]
                elif capacity > largest_key:
                    value = value + (largest_val * largest_key)
                else:
                    pass
    
        return value
    #method 2
    def get_optimal_value(capacity, weights, wvalues):

        value = 0.
        #more time
        cost_dict = dict()
        for wvalue, weight in zip(wvalues, weights):
            cost_dict[weight] = (wvalue / weight)
        while cost_dict and capacity>0:
            largest_key = max(cost_dict, key=cost_dict.get)
            largest_val = cost_dict[largest_key]
            if largest_key <= capacity:
                value = value + (largest_val * largest_key)
                capacity = capacity - largest_key
                cost_dict[largest_key] = 0
            elif capacity > largest_key:
                value = value + (largest_val * largest_key)
    
        return value
    # method 3
    # more time 10/5
    #more time
    def get_optimal_value(capacity, weights, wvalues):
  
        value = 0.
        cost_dict = dict()
        for wvalue, weight in zip(wvalues, weights):
            cost_dict[weight] = (wvalue / weight)
        while capacity>0:
            #if not bool(cost_dict):
            #    break
            largest_key = max(cost_dict, key=cost_dict.get)
            largest_val = cost_dict[largest_key]
            if largest_key <= capacity:
                 value = value + (largest_val * largest_key)
                capacity = capacity - largest_key
                cost_dict[largest_key] = 0
            elif capacity > largest_key:
                value = value + (largest_val * largest_key)
    
        return value

    # method 4
    # more time 10/5
    def get_optimal_value(capacity, weights, wvalues):

        value = 0.
  
        cost_dict = dict()
        if not bool(weights) or not bool(wvalues):
            return value
        for wvalue, weight in zip(wvalues, weights):
            cost_dict[weight] = (wvalue / weight)
    
        while capacity>0:
            largest_key = max(cost_dict, key=cost_dict.get)
            largest_val = cost_dict[largest_key]
            if largest_key <= capacity:
                value = value + (largest_val * largest_key)
                capacity = capacity - largest_key
                cost_dict[largest_key] = 0
            elif capacity > largest_key:
                value = value + (largest_val * largest_key)

        return value

    # method 5
    def foo(d,capacity):
    cost_dict = d
    largest_key = max(cost_dict, key=cost_dict.get)
    largest_val = cost_dict[largest_key]
    print(cost_dict, largest_key, largest_val,capacity)
    if largest_key <= capacity:
        value = (largest_val * largest_key)
        capacity = capacity - largest_key
        cost_dict[largest_key] = 0
    elif capacity > largest_key:
        value = (largest_val * largest_key)
    return value, capacity
    
    def get_optimal_value(capacity, weights, wvalues):

    value = 0.
  
    cost_dict = dict()
    if not bool(weights) or not bool(wvalues):
        return value
    for wvalue, weight in zip(wvalues, weights):
        cost_dict[weight] = (wvalue / weight)
    
    while capacity>0:
        val, capacity = foo(cost_dict, capacity)
        value = val + value
    return value
    """
