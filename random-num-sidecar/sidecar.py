from ndn.app import NDNApp
from ndn.encoding import Name, InterestParam, BinaryStr, FormalName, MetaInfo, Component, ContentType

import os
import time


app = NDNApp()

service_name = str(os.getenv('SERVICE_NAME'))
path_semaphore = '/shared/semaphore'
path_data = '/shared/data'

@app.route(service_name)
def on_interest(name: FormalName, param: InterestParam, _app_param):
    print(f'{time.time()}: interest arrives {Name.to_str(name)}, {param}')
    random_num = int(call_service())
    app.put_data(name, content=str(random_num).encode(),
                freshness_period=1000,
                final_block_id=Component.from_segment(0))

def call_service():
    while os.path.exists(path_semaphore):
        print(f'{time.time()}: service is busy now')
        time.sleep(1)

    print(f'{time.time()}: calling service')
    with open(path_data, 'w') as f:
        f.write('')

    with open(path_semaphore, 'w') as f:
        f.write('')

    #
    # SERVICE FUNCTON PROCESS
    #

    while os.path.exists(path_semaphore):
        time.sleep(1)

    with open(path_data, 'r') as f:
        data = f.read()
    print(f'{time.time()}: done')

    return data

if __name__ == '__main__':
    app.run_forever()
