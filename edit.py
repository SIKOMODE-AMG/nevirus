import json

# 1. Открываем и читаем существующий JSON
with open('config.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

# 2. Редактируем данные (работаем как с обычным словарем Python)
data['user_name'] = 'Иван'
data['status'] = 'active'
data['new_parameter'] = 123  # Можно добавлять новые ключи

# 3. Сохраняем измененные данные обратно в тот же файл
with open('config.json', 'w', encoding='utf-8') as file:
    json.dump(data, file, ensure_ascii=False, indent=4)

print("Файл успешно отредактирован!")