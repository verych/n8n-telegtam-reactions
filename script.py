
# Создание структуры кастомной ноды n8n для добавления реакций к постам Telegram

telegram_reaction_node_code = '''
import {
    IExecuteFunctions,
    INodeExecutionData,
    INodeType,
    INodeTypeDescription,
    NodeApiError,
} from 'n8n-workflow';

export class TelegramReaction implements INodeType {
    description: INodeTypeDescription = {
        displayName: 'Telegram Reaction',
        name: 'telegramReaction',
        icon: 'file:telegram.svg',
        group: ['transform'],
        version: 1,
        subtitle: '={{$parameter["operation"]}}',
        description: 'Add reactions to Telegram messages',
        defaults: {
            name: 'Telegram Reaction',
        },
        inputs: ['main'],
        outputs: ['main'],
        credentials: [
            {
                name: 'telegramApi',
                required: true,
            },
        ],
        properties: [
            {
                displayName: 'Operation',
                name: 'operation',
                type: 'options',
                noDataExpression: true,
                options: [
                    {
                        name: 'Set Reaction',
                        value: 'setReaction',
                        description: 'Add reactions to a message',
                        action: 'Set reactions to a message',
                    },
                ],
                default: 'setReaction',
            },
            {
                displayName: 'Chat ID',
                name: 'chatId',
                type: 'string',
                default: '',
                required: true,
                description: 'Unique identifier for the target chat or username (@channelusername)',
                placeholder: '@my_channel or -1001234567890',
            },
            {
                displayName: 'Message ID',
                name: 'messageId',
                type: 'number',
                default: 0,
                required: true,
                description: 'Identifier of the message to react to',
                placeholder: '123',
            },
            {
                displayName: 'Reactions',
                name: 'reactions',
                type: 'fixedCollection',
                typeOptions: {
                    multipleValues: true,
                },
                default: {},
                description: 'List of reactions to set on the message',
                placeholder: 'Add Reaction',
                options: [
                    {
                        name: 'reactionValues',
                        displayName: 'Reaction',
                        values: [
                            {
                                displayName: 'Reaction Type',
                                name: 'type',
                                type: 'options',
                                options: [
                                    {
                                        name: 'Emoji',
                                        value: 'emoji',
                                    },
                                    {
                                        name: 'Custom Emoji',
                                        value: 'custom_emoji',
                                    },
                                ],
                                default: 'emoji',
                                description: 'Type of reaction',
                            },
                            {
                                displayName: 'Emoji',
                                name: 'emoji',
                                type: 'options',
                                displayOptions: {
                                    show: {
                                        type: ['emoji'],
                                    },
                                },
                                options: [
                                    { name: '👍', value: '👍' },
                                    { name: '👎', value: '👎' },
                                    { name: '❤️', value: '❤️' },
                                    { name: '🔥', value: '🔥' },
                                    { name: '🥰', value: '🥰' },
                                    { name: '👏', value: '👏' },
                                    { name: '😁', value: '😁' },
                                    { name: '🤔', value: '🤔' },
                                    { name: '🤯', value: '🤯' },
                                    { name: '😱', value: '😱' },
                                    { name: '🤬', value: '🤬' },
                                    { name: '😢', value: '😢' },
                                    { name: '🎉', value: '🎉' },
                                    { name: '🤩', value: '🤩' },
                                    { name: '🤮', value: '🤮' },
                                    { name: '💩', value: '💩' },
                                    { name: '🙏', value: '🙏' },
                                    { name: '👌', value: '👌' },
                                    { name: '🕊', value: '🕊' },
                                    { name: '🤡', value: '🤡' },
                                    { name: '🥱', value: '🥱' },
                                    { name: '🥴', value: '🥴' },
                                    { name: '😍', value: '😍' },
                                    { name: '🐳', value: '🐳' },
                                    { name: '❤️‍🔥', value: '❤️‍🔥' },
                                    { name: '🌚', value: '🌚' },
                                    { name: '🌭', value: '🌭' },
                                    { name: '💯', value: '💯' },
                                    { name: '🤣', value: '🤣' },
                                    { name: '⚡️', value: '⚡️' },
                                    { name: '🍌', value: '🍌' },
                                    { name: '🏆', value: '🏆' },
                                    { name: '💔', value: '💔' },
                                    { name: '🤨', value: '🤨' },
                                    { name: '😐', value: '😐' },
                                    { name: '🍓', value: '🍓' },
                                    { name: '🍾', value: '🍾' },
                                    { name: '💋', value: '💋' },
                                    { name: '🖕', value: '🖕' },
                                    { name: '😈', value: '😈' },
                                    { name: '😴', value: '😴' },
                                    { name: '😭', value: '😭' },
                                    { name: '🤓', value: '🤓' },
                                    { name: '👻', value: '👻' },
                                    { name: '👨‍💻', value: '👨‍💻' },
                                    { name: '👀', value: '👀' },
                                    { name: '🎃', value: '🎃' },
                                    { name: '🙈', value: '🙈' },
                                    { name: '😇', value: '😇' },
                                    { name: '😨', value: '😨' },
                                    { name: '🤝', value: '🤝' },
                                    { name: '✍️', value: '✍️' },
                                    { name: '🤗', value: '🤗' },
                                    { name: '🫡', value: '🫡' },
                                    { name: '🎅', value: '🎅' },
                                    { name: '🎄', value: '🎄' },
                                    { name: '☃️', value: '☃️' },
                                    { name: '💅', value: '💅' },
                                    { name: '🤪', value: '🤪' },
                                    { name: '🗿', value: '🗿' },
                                    { name: '🆒', value: '🆒' },
                                    { name: '💘', value: '💘' },
                                    { name: '🙉', value: '🙉' },
                                    { name: '🦄', value: '🦄' },
                                    { name: '😘', value: '😘' },
                                    { name: '💊', value: '💊' },
                                    { name: '🙊', value: '🙊' },
                                    { name: '😎', value: '😎' },
                                    { name: '👾', value: '👾' },
                                    { name: '🤷‍♂️', value: '🤷‍♂️' },
                                    { name: '🤷', value: '🤷' },
                                    { name: '🤷‍♀️', value: '🤷‍♀️' },
                                    { name: '😡', value: '😡' },
                                ],
                                default: '👍',
                                description: 'Standard emoji reaction',
                            },
                            {
                                displayName: 'Custom Emoji ID',
                                name: 'customEmojiId',
                                type: 'string',
                                displayOptions: {
                                    show: {
                                        type: ['custom_emoji'],
                                    },
                                },
                                default: '',
                                description: 'Custom emoji identifier',
                                placeholder: '5368324170671202286',
                            },
                        ],
                    },
                ],
            },
            {
                displayName: 'Additional Options',
                name: 'additionalOptions',
                type: 'collection',
                placeholder: 'Add Option',
                default: {},
                options: [
                    {
                        displayName: 'Is Big',
                        name: 'isBig',
                        type: 'boolean',
                        default: false,
                        description: 'Whether to show reaction with a bigger animation',
                    },
                ],
            },
        ],
    };

    async execute(this: IExecuteFunctions): Promise<INodeExecutionData[][]> {
        const items = this.getInputData();
        const returnData: INodeExecutionData[] = [];
        const operation = this.getNodeParameter('operation', 0) as string;

        // Get credentials
        const credentials = await this.getCredentials('telegramApi');
        const token = credentials.accessToken as string;

        for (let i = 0; i < items.length; i++) {
            try {
                if (operation === 'setReaction') {
                    const chatId = this.getNodeParameter('chatId', i) as string;
                    const messageId = this.getNodeParameter('messageId', i) as number;
                    const reactions = this.getNodeParameter('reactions', i) as {
                        reactionValues?: Array<{
                            type: string;
                            emoji?: string;
                            customEmojiId?: string;
                        }>;
                    };
                    const additionalOptions = this.getNodeParameter('additionalOptions', i) as {
                        isBig?: boolean;
                    };

                    // Build reaction array
                    const reactionArray: Array<{ type: string; emoji?: string; custom_emoji_id?: string }> = [];

                    if (reactions.reactionValues && reactions.reactionValues.length > 0) {
                        reactions.reactionValues.forEach((reaction) => {
                            if (reaction.type === 'emoji' && reaction.emoji) {
                                reactionArray.push({
                                    type: 'emoji',
                                    emoji: reaction.emoji,
                                });
                            } else if (reaction.type === 'custom_emoji' && reaction.customEmojiId) {
                                reactionArray.push({
                                    type: 'custom_emoji',
                                    custom_emoji_id: reaction.customEmojiId,
                                });
                            }
                        });
                    }

                    // Prepare request body
                    const body: {
                        chat_id: string | number;
                        message_id: number;
                        reaction?: Array<{ type: string; emoji?: string; custom_emoji_id?: string }>;
                        is_big?: boolean;
                    } = {
                        chat_id: chatId,
                        message_id: messageId,
                    };

                    // Add reactions if provided
                    if (reactionArray.length > 0) {
                        body.reaction = reactionArray;
                    }

                    // Add is_big option if set
                    if (additionalOptions.isBig) {
                        body.is_big = true;
                    }

                    // Make API request
                    const response = await this.helpers.httpRequest({
                        method: 'POST',
                        url: `https://api.telegram.org/bot${token}/setMessageReaction`,
                        body,
                        json: true,
                    });

                    if (response.ok) {
                        returnData.push({
                            json: {
                                success: true,
                                chatId,
                                messageId,
                                reactions: reactionArray,
                                response,
                            },
                            pairedItem: { item: i },
                        });
                    } else {
                        throw new NodeApiError(this.getNode(), response, {
                            message: `Telegram API error: ${response.description || 'Unknown error'}`,
                        });
                    }
                }
            } catch (error) {
                if (this.continueOnFail()) {
                    returnData.push({
                        json: {
                            error: error.message,
                        },
                        pairedItem: { item: i },
                    });
                    continue;
                }
                throw error;
            }
        }

        return [returnData];
    }
}
'''

# Сохраняем код в файл
with open('TelegramReaction.node.ts', 'w', encoding='utf-8') as f:
    f.write(telegram_reaction_node_code)

print("✓ Создан файл: TelegramReaction.node.ts")
print(f"✓ Размер кода: {len(telegram_reaction_node_code)} символов")
