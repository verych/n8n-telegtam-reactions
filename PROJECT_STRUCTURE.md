# Структура проекта n8n-nodes-telegram-reaction

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
