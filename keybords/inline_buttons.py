from aiogram.types import (
    InlineKeyboardMarkup,
    InlineKeyboardButton
)


async def start_keyboard():
    markup = InlineKeyboardMarkup()
    questionnaire_button = InlineKeyboardButton(
        "Start Questionnaire",
        callback_data="start_questionnaire"
    )
    form_start_button = InlineKeyboardButton(
        "Registration",
        callback_data="fsm_start_form"
    )
    random_profiles_button = InlineKeyboardButton(
        "View User Forms",
        callback_data="random_profile"
    )
    profile_button = InlineKeyboardButton(
        "My Profile",
        callback_data="my_profile"
    )
    news_button = InlineKeyboardButton(
        "5 latest News",
        callback_data="Latest news"
    )


    markup.add(
        questionnaire_button
    ).add(
        form_start_button
    ).add(
        random_profiles_button
    ).add(
        profile_button
    ).add(
        news_button
    )
    return markup


async def question_first_keyboard():
    markup = InlineKeyboardMarkup()
    male_button = InlineKeyboardButton(
        "Male",
        callback_data="male_answer"
    )
    female_button = InlineKeyboardButton(
        "Female",
        callback_data="female_answer"
    )
    markup.add(
        male_button
    ).add(
        female_button
    )
    return markup


async def my_profile_keyboard():
    markup = InlineKeyboardMarkup()
    profile_button = InlineKeyboardButton(
        "My Profile",
        callback_data="my_profile"
    )

    markup.add(
        profile_button
    )
    return markup



async def like_dislike_keyboard(telegram_id):
    markup = InlineKeyboardMarkup()
    like_button = InlineKeyboardButton(
        "like",
        callback_data=f"_like_{telegram_id}"
    )

    dislike_button = InlineKeyboardButton(
        "dislike",
        callback_data="random_profile"
    )

    markup.add(
        like_button
    ).add(
        dislike_button
    )
    return markup


async def edit_delete_keyboard():
    markup = InlineKeyboardMarkup()
    update_button = InlineKeyboardButton(
        "Edit",
        callback_data=f"edit_profile"
    )

    delete_button = InlineKeyboardButton(
        "delete",
        callback_data="delete_profile"
    )

    markup.add(
        update_button
    ).add(
        delete_button
    )
    return markup


async def register_keyboard():
    markup = InlineKeyboardMarkup()
    form_start_button = InlineKeyboardButton(
        "Registration",
        callback_data="fsm_start_form"
    )
    markup.add(
        form_start_button
    )
    return markup