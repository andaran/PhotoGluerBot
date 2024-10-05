TOKEN = ""

HELLO_STICKERS = ('CAACAgIAAxkBAAEFVUli2TZykG2iYrlkfJllHNwYB0AQKwACBQADwDZPE_lqX5qCa011KQQ',
                  'CAACAgIAAxkBAAEFVUti2TbgS1QccVMs7uKxtjX285srhwAClwADO2AkFLPjVSHrbN7ZKQQ',
                  'CAACAgIAAxkBAAEFVU9i2Tb_j3Di5m1XJB7CWQ7mcRU2OQACHgkAAhhC7gj5WNnuHSGcISkE',
                  'CAACAgIAAxkBAAEFVVti2T1qPxhmexShMwnXnlKHREC2cwAC_AAD9wLID-JKwmellSruKQQ',
                  'CAACAgIAAxkBAAEFVV9i2T2t0is-XAu8v1TSHDB2-92kNwACmgAD9wLID9HVBvL9etQ4KQQ', )

HELLO_MESSAGE_1 = """
Привет! Я могу склеить несколько фотографий в одну большую.
Для этого отправь мне фотографии в виде файлов (файл -> галерея). 
Файлы можно отправлять по одному или несколько сразу.
После этого напиши /glue и я склею их.
Обрати внимание, что я храню фото только в течение 10 минут.
"""

HELLO_MESSAGE_2 = """
Чтобы настроить параметры склеивания, пришли их в обычном сообщении в формате JSON\. Например:
`{
    // Ширина готового изображения
    "width": 1000,

    // Толщина разделителя
    "margin": 0,

    // Цвет разделителя 
    "margin_color": "white"
}`
Эти параметры будут использоваться для всех последующих склеиваний\. Чтобы посмотреть свои текущие настройки, напиши /settings\.
"""

SETTINGS_PARAMS_TYPES = {
    "width": int,
    "margin": int,
    "margin_color": str,
}
