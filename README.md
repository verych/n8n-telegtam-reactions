# n8n-nodes-telegram-reaction

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
