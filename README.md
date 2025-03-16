# Подготовка виртуальной машины

## Склонируйте репозиторий

Склонируйте репозиторий проекта:

```bash
git clone https://github.com/yandex-praktikum/mle-project-sprint-4-v001.git
```

## Активируйте виртуальное окружение

Используйте то же самое виртуальное окружение, что и созданное для работы с уроками. Если его не существует, то его следует создать.

Создать новое виртуальное окружение можно командой:

```bash
python3 -m venv env_recsys_start
```

После его инициализации следующей командой

```bash
. env_recsys_start/bin/activate
```

установите в него необходимые Python-пакеты следующей командой

```bash
pip install -r requirements.txt
```

### Скачайте файлы с данными

Для начала работы понадобится три файла с данными:
- [tracks.parquet](https://storage.yandexcloud.net/mle-data/ym/tracks.parquet)
- [catalog_names.parquet](https://storage.yandexcloud.net/mle-data/ym/catalog_names.parquet)
- [interactions.parquet](https://storage.yandexcloud.net/mle-data/ym/interactions.parquet)
 
Скачайте их в директорию локального репозитория. Для удобства вы можете воспользоваться командой wget:

```bash
wget https://storage.yandexcloud.net/mle-data/ym/tracks.parquet

wget https://storage.yandexcloud.net/mle-data/ym/catalog_names.parquet

wget https://storage.yandexcloud.net/mle-data/ym/interactions.parquet
```

## Запустите Jupyter Lab

Запустите Jupyter Lab в командной строке

```bash
jupyter lab --ip=0.0.0.0 --no-browser
```

# Расчёт рекомендаций

Код для выполнения первой части проекта находится в файле `recommendations.ipynb`. Изначально, это шаблон. Используйте его для выполнения первой части проекта.

# Сервис рекомендаций

Код сервиса рекомендаций находится в файле `recommendation_service.py`.
Код класса рекоммендаций для основного сервиса находится в файле `recommendation_class.py`
Код сервиса для получения похожих обьектов для item_id находится в файле `features_service.py`
Код сервиса для сохранения и получения истории взаимодействий пользователя находится в файле `events_service.py`

# Необходимые команды для запуска всех сервисов

Терминал 1: 
```bash
source env_recsys_start/bin/activate
cd mle-project-sprint-4-v001/
uvicorn recommendation_service:app
```

Терминал 2:
```bash
source env_recsys_start/bin/activate
cd mle-project-sprint-4-v001/
uvicorn features_service:app --port 8010
```

Терминал 3:
```bash
source env_recsys_start/bin/activate
cd mle-project-sprint-4-v001/
uvicorn events_service:app --port 8020
```

# Инструкции для тестирования сервиса

Код для тестирования сервиса находится в файле `test_service.py`.

Терминал 4:

```bash
source env_recsys_start/bin/activate
cd mle-project-sprint-4-v001/
python test_service.py
```

Логи тестирования сервиса находятся в файле test_service.log
Туда записываются рекоммендации для пользователей 3-х разных типов


# Перемешивание

Логика перемешивания реализована так же как в задачах из теории спринта.
На четных местах стоят онлайн рекоммендации, на нечетных офлайн