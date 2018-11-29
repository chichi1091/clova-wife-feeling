from flask import Flask, request, jsonify
import logging
from logging import getLogger, StreamHandler, Formatter
import cek

logger = getLogger("LogTest")
app = Flask(__name__)

clova = cek.Clova(
    application_id="xxxxxxxx",
    default_language="ja",
    debug_mode=True)

# /clova に対してのPOSTリクエストを受け付けるサーバーを立てる
@app.route('/clova', methods=['POST'])
def my_service():
    body_dict = clova.route(body=request.data, header=request.headers)
    response = jsonify(body_dict)
    response.headers['Content-Type'] = 'application/json;charset-UTF-8'
    return response

# 起動時の処理
@clova.handle.launch
def launch_request_handler(clova_request):
    welcome_japanese = cek.Message(message="調子どうだい？", language="ja")
    response = clova.response([welcome_japanese])
    return response

# WifeStatusIntentの発火箇所
@clova.handle.intent("WifeStatusIntent")
def wife_status_handler(clova_request):
    print("ワイフインテント")
    slot = clova_request.slot_value("status")

    if slot == None:
        message_japanese = cek.Message(message="もう一回言って下さい", language="ja")
    elif u"気分" in slot:
        message_japanese = cek.Message(message="Clovaの気分はいい感じです", language="ja")
    elif u"欲しい物" in slot:
        message_japanese = cek.Message(message="Clovaはお金がほしいです", language="ja")
    else:
        message_japanese = cek.Message(message="もう一回言って下さい", language="ja")

    response = clova.response([message_japanese])
    return response

# 終了時
@clova.handle.end
def end_handler(clova_request):
    # Session ended, this handler can be used to clean up
    logger.info("Session ended.")

# 認識できなかった場合
@clova.handle.default
def default_handler(request):
    return clova.response("Sorry I don't understand! Could you please repeat?")

if __name__ == '__main__':
    app.run()