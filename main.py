from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ContextTypes
import
import os

print("Bot está rodando no Railway...")  # Isto ajudará a saber se o código está sendo executado.

# Definir o deck de cartas (links para imagens no Google Drive)
deck_de_cartas = [
    "https://drive.google.com/file/d/1X9KqD-oAfhXDbfEkJEdU_3H4vMQoE87O/view?usp=drive_link",
        "https://drive.google.com/file/d/1jX-_W6kgfLFRu1G0DMdhbVsa3MoGBORy/view?usp=drive_link",
        "https://drive.google.com/file/d/1AqE7k1tuJuAiHdK08IDb8MVP6f-Sw79m/view?usp=drive_link",
        "https://drive.google.com/file/d/1J6AiqQigJDuCFu5wcVehqyzKXEiiSDvB/view?usp=drive_link",
        "https://drive.google.com/file/d/1xQXypSvxCQrlXge_Fial9IlRK525YrQd/view?usp=drive_link",
        "https://drive.google.com/file/d/1tKPOoCVcq0-Av3TNHuTQjFfhpRpd8Na0/view?usp=drive_link",
        "https://drive.google.com/file/d/10C5wAofjeHnSRpEmbCeNiVLcHcWE2oAl/view?usp=drive_link",
        "https://drive.google.com/file/d/1YuUckJF7ZVCAEc8i8pbE33F1HXtxRcDd/view?usp=drive_link",
        "https://drive.google.com/file/d/1vLwkuyycIU9Dd3MQ5HW5QXwkP4_ik9Ct/view?usp=drive_link",
        "https://drive.google.com/file/d/1_7xZ3nsFNTYUH46hk_0nYPgGFYiz4qBh/view?usp=drive_link",
        "https://drive.google.com/file/d/1FmZ7AaZcT2EE1huzIYJmRbleDtWOQndJ/view?usp=drive_link",
        "https://drive.google.com/file/d/15fRVcxOmE4v77eaSupV8bfwI_8Df9vuV/view?usp=drive_link",
        "https://drive.google.com/file/d/1syWX0g0KMUssd0kLXUrn5eieGSJm0ULl/view?usp=drive_link",
        "https://drive.google.com/file/d/1BuhJJOuyRoteId9aE0c5Sh3EboqsJXOy/view?usp=drive_link",
        "https://drive.google.com/file/d/1GON89Tt-MuM7EPnn_jYqGhcm-cn6lHuf/view?usp=drive_link",
        "https://drive.google.com/file/d/1HJ7VYsSpb7WqOpQRwSAFiUW4EYFQpMnP/view?usp=drive_link",
        "https://drive.google.com/file/d/1I2nUTMQwC_0S4zh0NT8uHR3wLfd5P8oV/view?usp=drive_link",
        "https://drive.google.com/file/d/1HFLTjCoBL18GhixPqxQSj5WNZkcI--Jt/view?usp=drive_link",
        "https://drive.google.com/file/d/108tJN2fLbM6ROGy2rXKFGdxWW183ypDF/view?usp=drive_link",
        "https://drive.google.com/file/d/12iRFIw0WDDiU149cllKciYYq0QEtwPW7/view?usp=drive_link",
        "https://drive.google.com/file/d/18zRUjkVQytcuUK0uKYmzXL3cR6oE1TbT/view?usp=drive_link",
        "https://drive.google.com/file/d/1I59ywG8N9r3uXR8GhdnseUD9eEaNjs1Y/view?usp=drive_link",
        "https://drive.google.com/file/d/1COFpgEO8KhO9JHCAk1mVv9jDP_epmdjq/view?usp=drive_link",
        "https://drive.google.com/file/d/1o528ArEYw8XyAhb1QOTBVYrXp-WwE45n/view?usp=drive_link",
        "https://drive.google.com/file/d/15p8_mfsHuZVkd-nDEJzsdx6YdmkhXCIC/view?usp=drive_link",
        "https://drive.google.com/file/d/1XylDR5TuU4Gmw9MRhphXYhF5txg-Z8nu/view?usp=drive_link",
        "https://drive.google.com/file/d/1WyeXupPoiSP4L2xQT3h1U2Iglk9kKpUs/view?usp=drive_link",
        "https://drive.google.com/file/d/1cU_XIRc4Fy3gEB34xOLdxhXWwle9NeCJ/view?usp=drive_link",
        "https://drive.google.com/file/d/1ZT3x22nKJ-M69Kim5Syfc48hhkciTRn3/view?usp=drive_link",
        "https://drive.google.com/file/d/1D6LyfSmEmGrkFmaroOeCG_WVpH7Ez56M/view?usp=drive_link",
        "https://drive.google.com/file/d/1gTDJCHxqDJBY0ayjz8WiahnnfphOnLIJ/view?usp=drive_link",
        "https://drive.google.com/file/d/1r6y7YXx3ogOOzMXX6GXKzAnmNF-O5Cpo/view?usp=drive_link",
        "https://drive.google.com/file/d/1DE_SpDdkQiOCXIovpMwjie693aRuhG8B/view?usp=drive_link",
        "https://drive.google.com/file/d/1mmjhW_bCCpWm7uDlKb9DK6Xl4cD_cBte/view?usp=drive_link",
]

# Variáveis globais para armazenar o estado do jogo
jogadores = []
jogo_em_andamento = False
informante_atual = None
pontos = {}


# Comando para iniciar um novo jogo
async def novojogo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global jogo_em_andamento
    if jogo_em_andamento:
        await update.message.reply_text("Já há um jogo em andamento.")
        return
    await update.message.reply_text("Jogo iniciado! Quem vai jogar? Escreva /euvou para participar.")
    jogo_em_andamento = True


# Comando para os jogadores se inscreverem no jogo
async def euvou(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if not jogo_em_andamento:
        await update.message.reply_text("Não há jogo iniciado no momento. Use /novojogo para iniciar.")
        return
    jogador_nome = update.message.from_user.first_name  # Usando o nome real do jogador
    jogador_username = update.message.from_user.username  # Nome de usuário opcional
    jogador = jogador_nome if not jogador_username else jogador_username  # Preferir o nome real, caso o username não esteja configurado
    if jogador not in jogadores:
        jogadores.append(jogador)
        await update.message.reply_text(f"{jogador} se inscreveu no jogo!")
    else:
        await update.message.reply_text(f"{jogador}, você já está no jogo.")


# Comando para iniciar o jogo
async def iniciarjogo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if len(jogadores) < 1:
        await update.message.reply_text("Precisa de pelo menos 2 jogadores para iniciar o jogo.")
        return
    global informante_atual
    informante_atual = random.choice(jogadores)  # Escolher o informante aleatoriamente
    await update.message.reply_text(f"O Informante da rodada é {informante_atual}.")

    # Exibir o botão para o informante escolher a carta
    keyboard = [[InlineKeyboardButton("Escolha sua carta", callback_data="escolher_carta")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("O Informante, escolha sua carta.", reply_markup=reply_markup)


# Comando para escolher carta
async def escolher_carta(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    jogador = query.from_user.username

    # Exibir as 6 cartas como opções de escolha
    keyboard = [
        [InlineKeyboardButton(f"Carta {i + 1}", callback_data=f"carta_{i}") for i in range(6)]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    # Enviar as cartas para o jogador ver
    if jogador == informante_atual:
        await query.edit_message_text("Você é o Informante, escolha uma carta e escreva sua dica.")
        # Mostrar as cartas com links de imagens
        media = [InputMediaPhoto(deck_de_cartas[i]) for i in range(6)]
        await query.message.reply_media_group(media)
    else:
        await query.edit_message_text("Escolha uma carta.")
        # Mostrar as cartas com links de imagens
        media = [InputMediaPhoto(deck_de_cartas[i]) for i in range(6)]
        await query.message.reply_media_group(media)

    # Mostrar o botão para escolher uma carta
    await query.message.reply_text("Clique em uma carta abaixo para escolher.")


# Função para lidar com a dica do informante
async def dica_informante(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # O informante escreve uma dica após escolher uma carta
    await update.message.reply_text("Dica enviada aos outros jogadores.")


# Função para gerar o final da rodada
async def finaliza_rodada(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # Avaliar as escolhas dos jogadores e distribuir pontos
    await update.message.reply_text("Rodada finalizada. Pontos distribuídos.")


# Comando para terminar o jogo
async def gg(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    global jogo_em_andamento
    jogo_em_andamento = False
    jogadores.clear()
    await update.message.reply_text("Jogo encerrado.")


# Função principal para configurar o bot
def main() -> None:
    # Configurar o Application e Dispatcher
    application = Application.builder().token("8149589328:AAGbv5KuzMBeGFDzI8sH1qSdyBwwe7F8W3Y").build()

    # Adicionar os handlers para os comandos
    application.add_handler(CommandHandler("novojogo", novojogo))
    application.add_handler(CommandHandler("euvou", euvou))
    application.add_handler(CommandHandler("iniciarjogo", iniciarjogo))
    application.add_handler(CommandHandler("gg", gg))
    application.add_handler(CallbackQueryHandler(escolher_carta, pattern="escolher_carta"))

    # Iniciar o bot
    application.run_polling()


if __name__ == '__main__':
    main()
# fim