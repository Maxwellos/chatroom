# encoding:utf-8

import json
import os
from common.log import logger

config = {
    "open_ai_api_key": "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",
    "wechaty_puppet_service_token": "127.0.0.1:8080",
    "single_chat_prefix": ["办开", "雪冬", "韩雪东", "东", "办卡"],
    "single_chat_reply_prefix": "[自动回复]",
    "friends_name_white_list": ["白春雨", '凯子', '小蒋'],
    "group_chat_prefix": ["@作为听众"],
    "group_name_white_list": ["嘴角上扬"],
    "image_create_prefix": ["画", "看", "找"],
    "conversation_max_tokens": 1000,
    "character_desc": "你是ChatGPT, 一个由OpenAI训练的大型语言模型, 你旨在回答并解决人们的任何问题，并且可以使用多种语言与人交流。"
}


def load_config():
    global config
    config_path = "config-template.json"
    if not os.path.exists(config_path):
        raise Exception('配置文件不存在，请根据config-template.json模板创建config.json文件')

    config_str = read_file(config_path)
    # 将json字符串反序列化为dict类型
    config = json.loads(config_str)
    logger.info("[INIT] load config: {}".format(config))


def get_root():
    return os.path.dirname(os.path.abspath(__file__))


def read_file(path):
    with open(path, mode='r', encoding='utf-8') as f:
        return f.read()


def conf():
    return config


if __name__ == '__main__':
    import openai

    # openai.api_type = "azure"
    openai.api_key = "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"
    response = openai.Completion.create(
        model="gpt-3.5-turbo",
        prompt="我能问你点问题么",
        temperature=0,
        max_tokens=100,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        # stop=["\n\n"]
    )
    # print the completion
    print(response.choices[0].text)
