import random
from config import THUMBNAIL_LOCAL_DIR
from config import THUMBNAIL_WEB_DIR
import tts_provider

random_code = random.randint(0, 1000000000)
tts_web_path = '%s%s_%s.mp3' % (THUMBNAIL_WEB_DIR, 'en', 'test')
tts_local_path = '%s%s_%s.mp3' % (THUMBNAIL_LOCAL_DIR, 'en', 'test')
print tts_local_path
print tts_web_path
tts_provider.google('en', "Senators meeting on Obama nominees ends without deal", tts_local_path)
