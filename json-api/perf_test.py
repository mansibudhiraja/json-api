import time

from controller.cache import ApiClient


def perf_test_parallel_api():
    api_client = ApiClient(1, 60)
    
    t1=time.perf_counter()
    for count in range(10):
        api_client.get_all_posts_by_tags("tech,health,politics,startups,science,design,culture,history")
    t2=time.perf_counter()
    print(f'Finished in {t2-t1} seconds')

if __name__=="__main__":
    perf_test_parallel_api()
