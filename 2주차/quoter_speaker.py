# 제작자가 공개한 공식 사용법이 제대로 동작하지 않아,
# 설치된 라이브러리의 기능을 호출한 것 (우회해서 사용)

# 사용 오픈소스: quoters 0.30
# 라이선스: MIT License
# 용도: 무작위 명언 데이터 조회
# 저장소: https://github.com/suman-kr/quoters

from quoters.extract_data import _fetch_offline_quotes
from quoters.enum import QuoteType
from gtts import gTTS

quote = _fetch_offline_quotes(QuoteType.QUOTE)
random_qoute = quote
tts = gTTS(random_qoute, lang='en', tld='com')
tts.save('random_qoute_tts.mp3')