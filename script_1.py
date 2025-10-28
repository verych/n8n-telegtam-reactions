
# Создание дополнительных файлов для полной структуры ноды

# 1. package.json
package_json = '''{
  "name": "n8n-nodes-telegram-reaction",
  "version": "1.0.0",
  "description": "n8n node for adding reactions to Telegram messages",
  "keywords": [
    "n8n-community-node-package",
    "n8n-node",
    "telegram",
    "reaction"
  ],
  "license": "MIT",
  "homepage": "",
  "author": {
    "name": "Your Name",
    "email": "your.email@example.com"
  },
  "repository": {
    "type": "git",
    "url": "https://github.com/yourusername/n8n-nodes-telegram-reaction.git"
  },
  "main": "index.js",
  "scripts": {
    "build": "tsc && gulp build:icons",
    "dev": "tsc --watch",
    "format": "prettier nodes --write",
    "lint": "eslint nodes package.json",
    "lintfix": "eslint nodes package.json --fix",
    "prepublishOnly": "npm run build && npm run lint -c .eslintrc.prepublish.js nodes package.json"
  },
  "files": [
    "dist"
  ],
  "n8n": {
    "n8nNodesApiVersion": 1,
    "credentials": [],
    "nodes": [
      "dist/nodes/TelegramReaction/TelegramReaction.node.js"
    ]
  },
  "devDependencies": {
    "@types/node": "^18.16.0",
    "@typescript-eslint/parser": "^5.59.1",
    "eslint": "^8.40.0",
    "eslint-plugin-n8n-nodes-base": "^1.12.0",
    "gulp": "^4.0.2",
    "n8n-workflow": "*",
    "prettier": "^2.8.8",
    "typescript": "^5.0.4"
  },
  "peerDependencies": {
    "n8n-workflow": "*"
  }
}'''

# 2. tsconfig.json
tsconfig_json = '''{
  "compilerOptions": {
    "target": "ES2019",
    "module": "commonjs",
    "lib": ["ES2019"],
    "moduleResolution": "node",
    "declaration": true,
    "outDir": "./dist",
    "rootDir": "./",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true,
    "resolveJsonModule": true
  },
  "include": ["nodes/**/*"],
  "exclude": ["node_modules", "dist"]
}'''

# 3. README.md
readme_md = '''# n8n-nodes-telegram-reaction

Это кастомная нода для n8n, которая позволяет добавлять реакции к сообщениям в Telegram.

## Возможности

- ✅ Добавление emoji-реакций к сообщениям
- ✅ Поддержка кастомных emoji
- ✅ Гибкая настройка ID поста и списка реакций
- ✅ Поддержка больших анимаций реакций
- ✅ Работа с каналами, группами и личными чатами
- ✅ Полная совместимость с существующими Telegram-нодами n8n

## Установка

### Установка в n8n Community

1. В n8n перейдите в Settings → Community Nodes
2. Нажмите "Install a community node"
3. Введите `n8n-nodes-telegram-reaction`
4. Нажмите "Install"

### Локальная установка для разработки

```bash
# Клонируйте репозиторий
git clone https://github.com/yourusername/n8n-nodes-telegram-reaction.git

# Перейдите в директорию
cd n8n-nodes-telegram-reaction

# Установите зависимости
npm install

# Соберите ноду
npm run build

# Свяжите ноду локально
npm link

# В директории вашего n8n
npm link n8n-nodes-telegram-reaction
```

## Использование

### Настройка учетных данных

Нода использует стандартные учетные данные Telegram Bot API:

1. Создайте бота через [@BotFather](https://t.me/BotFather)
2. Получите API token
3. В n8n добавьте credentials "Telegram API" с полученным токеном

### Параметры ноды

#### Обязательные параметры:

- **Chat ID**: ID чата, канала или username (@channel_name)
- **Message ID**: ID сообщения, к которому нужно добавить реакцию

#### Реакции:

Нода поддерживает добавление нескольких реакций одновременно:

- **Reaction Type**: 
  - `Emoji` - стандартные emoji-реакции
  - `Custom Emoji` - кастомные emoji (требуется Premium или разрешение администратора)

- **Emoji**: Выбор из 75+ доступных emoji-реакций, включая:
  - 👍 👎 ❤️ 🔥 🥰 👏 😁 🤔 🤯 😱
  - 🎉 🤩 💩 🙏 👌 🤡 😍 💯 🤣 ⚡️
  - И многие другие...

- **Custom Emoji ID**: ID кастомного emoji (для premium пользователей)

#### Дополнительные опции:

- **Is Big**: Показывать реакцию с увеличенной анимацией

### Примеры использования

#### Пример 1: Добавление простой реакции

```json
{
  "chatId": "@my_channel",
  "messageId": 123,
  "reactions": {
    "reactionValues": [
      {
        "type": "emoji",
        "emoji": "👍"
      }
    ]
  }
}
```

#### Пример 2: Добавление нескольких реакций

```json
{
  "chatId": "-1001234567890",
  "messageId": 456,
  "reactions": {
    "reactionValues": [
      {
        "type": "emoji",
        "emoji": "❤️"
      },
      {
        "type": "emoji",
        "emoji": "🔥"
      },
      {
        "type": "emoji",
        "emoji": "🎉"
      }
    ]
  },
  "additionalOptions": {
    "isBig": true
  }
}
```

#### Пример 3: Использование в workflow

```
Telegram Trigger → IF → Telegram Reaction
```

Автоматически добавляет реакцию к сообщениям, содержащим определенные ключевые слова.

## API Reference

Нода использует официальный метод Telegram Bot API:
- [setMessageReaction](https://core.telegram.org/bots/api#setmessagereaction)

## Требования

- n8n версии 0.198.0 или выше
- Telegram Bot API 7.0+
- Бот должен иметь права администратора в канале/группе для добавления реакций

## Ограничения

- Боты могут добавлять только одну реакцию за раз (не-premium пользователи)
- Кастомные emoji требуют Premium или разрешения администратора
- Реакции работают не для всех типов сервисных сообщений

## Разработка

### Структура проекта

```
n8n-nodes-telegram-reaction/
├── nodes/
│   └── TelegramReaction/
│       ├── TelegramReaction.node.ts
│       └── telegram.svg
├── package.json
├── tsconfig.json
└── README.md
```

### Сборка

```bash
npm run build
```

### Линтинг

```bash
npm run lint
npm run lintfix
```

## Вклад в проект

Приветствуются pull requests! Для крупных изменений сначала откройте issue для обсуждения.

## Лицензия

[MIT](LICENSE)

## Поддержка

- 📧 Email: your.email@example.com
- 🐛 Issues: [GitHub Issues](https://github.com/yourusername/n8n-nodes-telegram-reaction/issues)
- 💬 Telegram: [@yourusername](https://t.me/yourusername)

## Связанные ресурсы

- [n8n Documentation](https://docs.n8n.io/)
- [Telegram Bot API](https://core.telegram.org/bots/api)
- [Creating n8n nodes](https://docs.n8n.io/integrations/creating-nodes/)
'''

# 4. Инструкция по установке
installation_guide = '''# Руководство по установке и настройке ноды Telegram Reaction

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
'''

# Сохраняем файлы
files_created = []

with open('package.json', 'w', encoding='utf-8') as f:
    f.write(package_json)
    files_created.append('package.json')

with open('tsconfig.json', 'w', encoding='utf-8') as f:
    f.write(tsconfig_json)
    files_created.append('tsconfig.json')

with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme_md)
    files_created.append('README.md')

with open('INSTALLATION.md', 'w', encoding='utf-8') as f:
    f.write(installation_guide)
    files_created.append('INSTALLATION.md')

print("✓ Созданы файлы конфигурации и документации:")
for file in files_created:
    print(f"  - {file}")
