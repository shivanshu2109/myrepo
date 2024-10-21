def LIFO_FF(k, n, m, requests):
    #Calculates the number of cache misses for LIFO and FF algorithms.
    #Input:
    #  k: size of the cache.
    #  n: number of pages.
    #  m: number of page requests.
    #Returns:
    #  A tuple containing the sum and difference of LIFO and FF misses.

    def LIFO(requests):
        cache = {}
        stack = []
        misses = 0
        for page in requests:
            if page not in cache:
                misses += 1
                if len(cache) == k:
                    evicted_page = stack.pop()
                    del cache[evicted_page]
                cache[page] = True
                stack.append(page)
        return misses

    def FF(requests):
        cache = {}
        next_access = [m] * (n + 1)  
        for i in range(m - 1, -1, -1):
            page = requests[i]
            next_access[page] = i
        misses = 0
        for i in range(m):
            page = requests[i]
            if page not in cache:
                misses += 1
                if len(cache) == k:
                    furthest_page = None
                    furthest_access = -1
                    for p in cache:
                        if next_access[p] > furthest_access:
                            furthest_access = next_access[p]
                            furthest_page = p
                    del cache[furthest_page]
                cache[page] = True
        return misses

    lifo_misses = LIFO(requests)
    ff_misses = FF(requests)
    return lifo_misses + ff_misses, lifo_misses - ff_misses


def read_input():
    k, n, m = map(int, input().split())
    requests = []
    for _ in range(m):
        request = int(input())
        requests.append(request)
    return k, n, m, requests


if __name__ == "__main__":
    k, n, m, requests = read_input()
    sum, dif = LIFO_FF(k, n, m, requests)
    print(sum, dif)

def read_input():
    k, n, m = map(int, input().split())
    requests = []
    for _ in range(m):
        request = int(input())
        requests.append(request)
    return k, n, m, requests


if __name__ == "__main__":
    k, n, m, requests = read_input()
    sum, dif = LIFO_FF(k, n, m, requests)
    print(sum, dif)
