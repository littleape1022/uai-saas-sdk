import sys
import time
from api.create_to_frame_job import UAICensorCreateAsyncToFrameJobApi
from api.create_to_frame_job import ToFrameMode_FullCut
from api.utils import gen_signature, load_config

# usage: python create_async_toframe_job.py config_file='toframe-config.json'

if __name__ == '__main__':
    if len(sys.argv) == 2:
        config_file = sys.argv[1]
    else:
        config_file = 'toframe-config.json'
    timestamp = int(time.time())
    mode = ToFrameMode_FullCut
    url = 'http://uai-demo-adam.cn-bj.ufileos.com/face_test.mp4'
    bucket = 'bbh.ufile.ucloud.cn'
    prefix = 'sdk-'+str(timestamp)
    interval = 25
    callback = ''
    public_key, private_key, resource_id = load_config(config_file)
    signature = gen_signature(config_file=config_file,timestamp=timestamp, url=url)
    caller = UAICensorCreateAsyncToFrameJobApi(signature, public_key, resource_id,
                                             timestamp, mode, url, interval, bucket, prefix, callback)
    caller.call_api()