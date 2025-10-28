
# Создание дополнительного файла - структуры директорий и примера использования

# Структура проекта
project_structure = '''# Структура проекта n8n-nodes-telegram-reaction

```
n8n-nodes-telegram-reaction/
│
├── nodes/
│   └── TelegramReaction/
│       ├── TelegramReaction.node.ts      # Основной файл ноды
│       ├── TelegramReaction.node.json    # Codex file (metadata)
│       └── telegram.svg                   # Иконка ноды
│
├── package.json                           # Конфигурация npm пакета
├── tsconfig.json                          # Конфигурация TypeScript
├── README.md                              # Основная документация
├── INSTALLATION.md                        # Руководство по установке
├── LICENSE                                # Лицензия MIT
└── .gitignore                             # Git ignore файл
```

## Описание файлов

### TelegramReaction.node.ts
Основной файл ноды, содержит:
- Определение интерфейса INodeType
- Описание параметров ноды (description)
- Логику выполнения (execute method)
- Обработку API запросов к Telegram

### package.json
Определяет:
- Метаданные пакета
- Зависимости
- Точку входа для n8n
- Скрипты сборки и линтинга

### tsconfig.json
Настройки компилятора TypeScript для корректной сборки.
'''

# Codex file
codex_json = '''{
  "node": "n8n-nodes-telegram-reaction.telegramReaction",
  "nodeVersion": "1.0",
  "codexVersion": "1.0",
  "categories": ["Communication"],
  "resources": {
    "credentialDocumentation": [
      {
        "url": "https://core.telegram.org/bots#6-botfather"
      }
    ],
    "primaryDocumentation": [
      {
        "url": "https://github.com/yourusername/n8n-nodes-telegram-reaction"
      }
    ],
    "generic": [
      {
        "label": "Telegram Bot API",
        "url": "https://core.telegram.org/bots/api"
      }
    ]
  },
  "alias": ["Telegram", "Reaction", "Emoji"],
  "subcategories": {
    "Communication": ["Social Media"]
  }
}'''

# .gitignore
gitignore = '''# Dependencies
node_modules/
package-lock.json
npm-debug.log*

# Build output
dist/
*.js
*.js.map
*.d.ts

# IDE
.vscode/
.idea/
*.swp
*.swo
*~

# OS
.DS_Store
Thumbs.db

# Logs
logs/
*.log

# Environment
.env
.env.local

# Testing
coverage/
.nyc_output/
'''

# Пример workflow
example_workflow = '''{
  "name": "Telegram Reaction Example Workflow",
  "nodes": [
    {
      "parameters": {},
      "name": "When clicking Test workflow",
      "type": "n8n-nodes-base.manualTrigger",
      "typeVersion": 1,
      "position": [250, 300]
    },
    {
      "parameters": {
        "operation": "setReaction",
        "chatId": "@my_channel",
        "messageId": 123,
        "reactions": {
          "reactionValues": [
            {
              "type": "emoji",
              "emoji": "👍"
            },
            {
              "type": "emoji",
              "emoji": "❤️"
            }
          ]
        },
        "additionalOptions": {
          "isBig": true
        }
      },
      "name": "Telegram Reaction",
      "type": "n8n-nodes-telegram-reaction.telegramReaction",
      "typeVersion": 1,
      "position": [450, 300],
      "credentials": {
        "telegramApi": {
          "id": "1",
          "name": "Telegram Bot"
        }
      }
    }
  ],
  "connections": {
    "When clicking Test workflow": {
      "main": [
        [
          {
            "node": "Telegram Reaction",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "settings": {}
}'''

# Advanced example workflow
advanced_workflow = '''{
  "name": "Auto-React to Telegram Messages",
  "nodes": [
    {
      "parameters": {
        "updates": ["message"]
      },
      "name": "Telegram Trigger",
      "type": "n8n-nodes-base.telegramTrigger",
      "typeVersion": 1,
      "position": [250, 300],
      "webhookId": "telegram-webhook",
      "credentials": {
        "telegramApi": {
          "id": "1",
          "name": "Telegram Bot"
        }
      }
    },
    {
      "parameters": {
        "conditions": {
          "string": [
            {
              "value1": "={{$json.message.text}}",
              "operation": "contains",
              "value2": "спасибо"
            }
          ]
        }
      },
      "name": "IF Contains Thank You",
      "type": "n8n-nodes-base.if",
      "typeVersion": 1,
      "position": [450, 300]
    },
    {
      "parameters": {
        "operation": "setReaction",
        "chatId": "={{$json.message.chat.id}}",
        "messageId": "={{$json.message.message_id}}",
        "reactions": {
          "reactionValues": [
            {
              "type": "emoji",
              "emoji": "🙏"
            },
            {
              "type": "emoji",
              "emoji": "❤️"
            }
          ]
        }
      },
      "name": "Add Thank You Reaction",
      "type": "n8n-nodes-telegram-reaction.telegramReaction",
      "typeVersion": 1,
      "position": [650, 200],
      "credentials": {
        "telegramApi": {
          "id": "1",
          "name": "Telegram Bot"
        }
      }
    },
    {
      "parameters": {
        "operation": "setReaction",
        "chatId": "={{$json.message.chat.id}}",
        "messageId": "={{$json.message.message_id}}",
        "reactions": {
          "reactionValues": [
            {
              "type": "emoji",
              "emoji": "👍"
            }
          ]
        }
      },
      "name": "Add Default Reaction",
      "type": "n8n-nodes-telegram-reaction.telegramReaction",
      "typeVersion": 1,
      "position": [650, 400],
      "credentials": {
        "telegramApi": {
          "id": "1",
          "name": "Telegram Bot"
        }
      }
    }
  ],
  "connections": {
    "Telegram Trigger": {
      "main": [
        [
          {
            "node": "IF Contains Thank You",
            "type": "main",
            "index": 0
          }
        ]
      ]
    },
    "IF Contains Thank You": {
      "main": [
        [
          {
            "node": "Add Thank You Reaction",
            "type": "main",
            "index": 0
          }
        ],
        [
          {
            "node": "Add Default Reaction",
            "type": "main",
            "index": 0
          }
        ]
      ]
    }
  },
  "settings": {}
}'''

# Сохраняем файлы
files_created = []

with open('PROJECT_STRUCTURE.md', 'w', encoding='utf-8') as f:
    f.write(project_structure)
    files_created.append('PROJECT_STRUCTURE.md')

with open('TelegramReaction.node.json', 'w', encoding='utf-8') as f:
    f.write(codex_json)
    files_created.append('TelegramReaction.node.json')

with open('.gitignore', 'w', encoding='utf-8') as f:
    f.write(gitignore)
    files_created.append('.gitignore')

with open('example-workflow-basic.json', 'w', encoding='utf-8') as f:
    f.write(example_workflow)
    files_created.append('example-workflow-basic.json')

with open('example-workflow-advanced.json', 'w', encoding='utf-8') as f:
    f.write(advanced_workflow)
    files_created.append('example-workflow-advanced.json')

print("✓ Созданы дополнительные файлы:")
for file in files_created:
    print(f"  - {file}")

# Создание сводной таблицы со всеми файлами
import csv

all_files = [
    ['Файл', 'Описание', 'Тип'],
    ['TelegramReaction.node.ts', 'Основной код ноды с логикой', 'TypeScript'],
    ['TelegramReaction.node.json', 'Метаданные ноды (codex)', 'JSON'],
    ['package.json', 'Конфигурация npm пакета', 'JSON'],
    ['tsconfig.json', 'Конфигурация TypeScript', 'JSON'],
    ['README.md', 'Основная документация', 'Markdown'],
    ['INSTALLATION.md', 'Руководство по установке', 'Markdown'],
    ['PROJECT_STRUCTURE.md', 'Структура проекта', 'Markdown'],
    ['.gitignore', 'Git ignore правила', 'Text'],
    ['example-workflow-basic.json', 'Базовый пример workflow', 'JSON'],
    ['example-workflow-advanced.json', 'Продвинутый пример workflow', 'JSON'],
]

with open('files-summary.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerows(all_files)

print("\n✓ Создана сводная таблица: files-summary.csv")
print("\n📦 Всего создано файлов: 11")
print("\n🎯 Нода полностью готова к использованию!")
