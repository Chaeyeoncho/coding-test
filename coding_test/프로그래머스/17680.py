def solution(cacheSize, cities):
    cities = [city.lower() for city in cities]
    cache = []
    answer = 0
    
    if cacheSize == 0: 
        return len(cities) * 5


    for city in cities:
        if city in cache:  # Hit
            answer += 1
            cache.remove(city)
            cache.append(city)
        else:  # Miss
            answer += 5
            if len(cache) >= cacheSize:
                cache.pop(0)
            cache.append(city)

    return answer
