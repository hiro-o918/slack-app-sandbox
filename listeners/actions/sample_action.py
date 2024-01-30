from logging import Logger

from slack_bolt import Ack
from slack_sdk import WebClient


def move_to_next_action_callback(ack: Ack, client: WebClient, body: dict, logger: Logger):
    try:
        ack()
        client.views_update(
            view_id=body["view"]["id"],
            hash=body["view"]["hash"],
            view={
                "type": "modal",
                "callback_id": "sample_view_id",
                "title": {
                    "type": "plain_text",
                    "text": "Move to next",
                },
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "Nice! You updated the modal! 🎉",
                        },
                    },
                    {
                        "type": "image",
                        "image_url": "https://media.giphy.com/media/SVZGEcYt7brkFUyU90/giphy.gif",
                        "alt_text": "Yay! The modal was updated",
                    },
                    {
                        "type": "input",
                        "block_id": "input_block_id",
                        "label": {
                            "type": "plain_text",
                            "text": "What are your hopes and dreams?",
                        },
                        "element": {
                            "type": "plain_text_input",
                            "action_id": "sample_input_id",
                            "multiline": True,
                        },
                    },
                    {
                        "block_id": "select_channel_block_id",
                        "type": "input",
                        "label": {
                            "type": "plain_text",
                            "text": "Select a channel to message the result to",
                        },
                        "element": {
                            "type": "conversations_select",
                            "action_id": "sample_dropdown_id",
                            "response_url_enabled": True,
                        },
                    },
                ],
                "submit": {"type": "plain_text", "text": "Submit"},
            },
        )
    except Exception as e:
        logger.error(e)


def sample_action_callback(ack: Ack, client: WebClient, body: dict, logger: Logger):
    try:
        ack()
        client.views_update(
            view_id=body["view"]["id"],
            hash=body["view"]["hash"],
            view={
                "type": "modal",
                "callback_id": "sample_view_id",
                "title": {
                    "type": "plain_text",
                    "text": "Update modal title",
                },
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "Nice! You updated the modal! 🎉",
                        },
                    },
                    {
                        "type": "image",
                        "image_url": "https://media.giphy.com/media/SVZGEcYt7brkFUyU90/giphy.gif",
                        "alt_text": "Yay! The modal was updated",
                    },
                    {
                        "type": "input",
                        "block_id": "input_block_id",
                        "label": {
                            "type": "plain_text",
                            "text": "What are your hopes and dreams?",
                        },
                        "element": {
                            "type": "plain_text_input",
                            "action_id": "sample_input_id",
                            "multiline": True,
                        },
                    },
                    {
                        "block_id": "select_channel_block_id",
                        "type": "input",
                        "label": {
                            "type": "plain_text",
                            "text": "Select a channel to message the result to",
                        },
                        "element": {
                            "type": "conversations_select",
                            "action_id": "sample_dropdown_id",
                            "response_url_enabled": True,
                        },
                    },
                ],
                "submit": {"type": "plain_text", "text": "Submit"},
            },
        )
    except Exception as e:
        logger.error(e)


def solved_action(ack: Ack, client: WebClient, body: dict, logger: Logger):
    try:
        ack()

        updated_message = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Solved!* :white_check_mark:",
                },
            },
        ]
        client.chat_postMessage(
            channel=body["container"]["channel_id"],
            thread_ts=body["message"]["ts"],
            text="solved!",
        )
        client.chat_update(
            channel=body["container"]["channel_id"],
            ts=body["message"]["ts"],
            blocks=body["message"]["blocks"][:-1] + updated_message,
        )
    except Exception as e:
        logger.error(e)


def pended_action(ack: Ack, client: WebClient, body: dict, logger: Logger):
    try:
        ack()
        updated_message = [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "*Pended!* :no_entry_sign:",
                },
            },
        ]
        client.chat_postMessage(
            channel=body["container"]["channel_id"],
            thread_ts=body["message"]["ts"],
            text="denied!",
        )
        client.chat_update(
            channel=body["container"]["channel_id"],
            ts=body["message"]["ts"],
            blocks=body["message"]["blocks"][:2] + updated_message,
        )
    except Exception as e:
        logger.error(e)
