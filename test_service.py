import requests
import logging

logging.basicConfig(
    filename="test_service.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

recommendations_url = "http://127.0.0.1:8000"
events_store_url = "http://127.0.0.1:8020"
headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}

def log_recommendations(test_case, recs_offline, recs_online, recs_blended):
    """Логирует результаты рекомендаций."""
    logging.info(f"=== {test_case} ===")
    logging.info(f"Офлайн: {recs_offline}")
    logging.info(f"Онлайн: {recs_online}")
    logging.info(f"Перемешанные: {recs_blended}")
    logging.info("=====================")

# Тест 1: Пользователь без персональных рекомендаций
user_id_no_personal = 999999999999
params = {"user_id": user_id_no_personal, 'k': 10}
resp_offline = requests.post(recommendations_url + "/recommendations_offline", headers=headers, params=params)
resp_online = requests.post(recommendations_url + "/recommendations_online", headers=headers, params=params)
resp_blended = requests.post(recommendations_url + "/recommendations", headers=headers, params=params)

recs_offline = resp_offline.json()["recs"]
recs_online = resp_online.json()["recs"]
recs_blended = resp_blended.json()["recs"]

log_recommendations("Тест 1: Пользователь без персональных рекомендаций", recs_offline, recs_online, recs_blended)

# Тест 2: Пользователь с персональными рекомендациями, но без онлайн-истории
user_id_personal_no_online = 684071
params = {"user_id": user_id_personal_no_online, 'k': 10}
resp_offline = requests.post(recommendations_url + "/recommendations_offline", headers=headers, params=params)
resp_online = requests.post(recommendations_url + "/recommendations_online", headers=headers, params=params)
resp_blended = requests.post(recommendations_url + "/recommendations", headers=headers, params=params)

recs_offline = resp_offline.json()["recs"]
recs_online = resp_online.json()["recs"]
recs_blended = resp_blended.json()["recs"]

log_recommendations("Тест 2: Пользователь с персональными рекомендациями, но без онлайн-истории", recs_offline, recs_online, recs_blended)

# Тест 3: Пользователь с персональными рекомендациями и онлайн-историей
user_id_personal_with_online = 711033
event_item_ids = [85192958, 62208587, 9047114, 18385776, 2758009]
for event_item_id in event_item_ids:
    requests.post(events_store_url + "/put", headers=headers, params={"user_id": user_id_personal_with_online, "item_id": event_item_id})

params = {"user_id": user_id_personal_with_online, 'k': 10}
resp_offline = requests.post(recommendations_url + "/recommendations_offline", headers=headers, params=params)
resp_online = requests.post(recommendations_url + "/recommendations_online", headers=headers, params=params)
resp_blended = requests.post(recommendations_url + "/recommendations", headers=headers, params=params)

recs_offline = resp_offline.json()["recs"]
recs_online = resp_online.json()["recs"]
recs_blended = resp_blended.json()["recs"]

log_recommendations("Тест 3: Пользователь с персональными рекомендациями и онлайн-историей", recs_offline, recs_online, recs_blended)