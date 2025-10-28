# Руководство по установке и настройке ноды Telegram Reaction

## Быстрый старт

### 1. Установка в существующий n8n

#### Вариант A: Установка через npm (рекомендуется)

```bash
cd ~/.n8n/nodes
npm install n8n-nodes-telegram-reaction
```

Перезапустите n8n:
```bash
n8n restart
```

#### Вариант B: Ручная установка для разработки

1. Клонируйте или скачайте репозиторий:
```bash
cd ~/.n8n/custom
git clone https://github.com/yourusername/n8n-nodes-telegram-reaction.git
cd n8n-nodes-telegram-reaction
```

2. Установите зависимости:
```bash
npm install
```

3. Соберите проект:
```bash
npm run build
```

4. Создайте символическую ссылку:
```bash
npm link
```

5. В директории n8n:
```bash
cd ~/.n8n
npm link n8n-nodes-telegram-reaction
```

6. Перезапустите n8n

### 2. Установка в Docker

Добавьте в ваш `docker-compose.yml`:

```yaml
version: '3'

services:
  n8n:
    image: n8nio/n8n
    restart: always
    ports:
      - "5678:5678"
    environment:
      - N8N_CUSTOM_EXTENSIONS=/data/custom
    volumes:
      - ~/.n8n:/home/node/.n8n
      - ./custom:/data/custom
```

Затем:

```bash
cd ./custom
git clone https://github.com/yourusername/n8n-nodes-telegram-reaction.git
cd n8n-nodes-telegram-reaction
npm install && npm run build
docker-compose restart
```

### 3. Настройка Telegram Bot

1. Откройте Telegram и найдите [@BotFather](https://t.me/BotFather)

2. Создайте нового бота:
```
/newbot
```

3. Следуйте инструкциям и получите API Token вида:
```
123456789:ABCdefGHIjklMNOpqrsTUVwxyz
```

4. (Опционально) Добавьте бота в канал/группу как администратора

### 4. Настройка credentials в n8n

1. Откройте n8n UI
2. Перейдите в `Credentials` → `New`
3. Найдите `Telegram API`
4. Вставьте ваш Bot Token
5. Нажмите `Save`

### 5. Первый workflow

1. Создайте новый workflow
2. Добавьте ноду `Telegram Reaction`
3. Выберите credentials
4. Настройте параметры:
   - Chat ID: ID вашего канала (например: `@my_channel` или `-1001234567890`)
   - Message ID: ID сообщения
   - Reactions: выберите emoji

5. Запустите workflow

## Получение Chat ID

### Для личных чатов:
1. Напишите боту `/start`
2. Используйте ноду `Telegram Trigger` для получения chat_id из сообщения

### Для каналов:
1. Добавьте бота как администратора
2. Используйте username канала: `@channel_name`
3. Или получите числовой ID через [@userinfobot](https://t.me/userinfobot)

### Для групп:
1. Добавьте бота в группу
2. Получите group_id через Telegram API или [@userinfobot](https://t.me/userinfobot)

## Получение Message ID

Message ID можно получить несколькими способами:

1. **Через Telegram Trigger ноду**: Message ID будет в поле `message.message_id`

2. **Вручную в Desktop Telegram**: 
   - Правый клик на сообщение → Copy Message Link
   - ID будет в конце ссылки: `https://t.me/channel/123` (123 - это ID)

3. **Через API**: Используйте метод `getUpdates` для получения последних сообщений

## Проверка установки

Выполните в консоли:

```bash
ls -la ~/.n8n/nodes/node_modules/ | grep telegram-reaction
```

Или в n8n UI найдите ноду `Telegram Reaction` в поиске нод.

## Устранение неполадок

### Нода не появляется в списке

1. Проверьте, что сборка прошла успешно:
```bash
npm run build
```

2. Проверьте логи n8n:
```bash
n8n start --log-level debug
```

3. Убедитесь, что путь к ноде правильный в package.json

### Ошибка "Bad Request: message to react not found"

- Проверьте, что Message ID правильный
- Убедитесь, что бот имеет доступ к сообщению
- Бот должен быть администратором в канале/группе

### Ошибка "Bot token is invalid"

- Проверьте, что токен скопирован полностью
- Токен должен быть от @BotFather
- Убедитесь, что бот не был удален

### Ошибка "Chat not found"

- Проверьте формат Chat ID
- Для каналов используйте `@username` или числовой ID
- Убедитесь, что бот добавлен в канал/группу

## Дополнительные ресурсы

- [Документация n8n по созданию кастомных нод](https://docs.n8n.io/integrations/creating-nodes/)
- [Telegram Bot API Documentation](https://core.telegram.org/bots/api)
- [n8n Community Forum](https://community.n8n.io/)
