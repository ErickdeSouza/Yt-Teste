from google_apis import create_service
import time
from pytube import Channel
import random
import os
from fastapi import FastAPI



links_canal = ['https://www.youtube.com/channel/UCdlJx-w37viXFNq__qZ7ARQ', 'https://www.youtube.com/channel/UC5mZsx_OVnc4XmG9rWU2p3A', 'https://www.youtube.com/channel/UCV306eHqgo0LvBf3Mh36AHg', 'https://www.youtube.com/channel/UCYzp8-P162Em-3uZnCuGJOg', 'https://www.youtube.com/channel/UCukwGwBD-pAbGzoJo6ZXPtQ', 'https://www.youtube.com/channel/UC6cALLZLWQGilBFBB0PWAog']


vistos = ['HtcsMu2v0VE', 'dGiElR-kxJk', 'oRwPXhhRWrk', 'S8VXWAc18Fs', 'UKb0kWcruT0', 'CRCmeneeqY0']
comentarios = []

cont = 0
CLIENT_FILE = 'client_secret.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = [
	'https://www.googleapis.com/auth/youtube',
	'https://www.googleapis.com/auth/youtube.force-ssl',
	'https://www.googleapis.com/auth/youtubepartner'
]

service = create_service(CLIENT_FILE, API_NAME, API_VERSION, SCOPES)




def comentar(id):
  global cont
  msgs = [f'ESSE CANAL DO {canal_nome} E UM LIXO KKKKKKKKKKKKKKKKKKKKKKKKK', f'Є𝙨𝙨Є 🇨∧𝙉∧𝙻 Ḋଠ {canal_nome} Є பᙢ 𝙻┃𝐱ଠ ķķķķķķķķķķķķķķķķķķķķķķķķķ', f'ᴱ⟆⟆ᴱ Ꞇ𝚨𝐍𝚨乚 DO {canal_nome} ᴱ ŰΜ 乚∤𝕩օ ᴋᴋᴋᴋᴋᴋᴋᴋᴋᴋᴋᴋᴋᴋᴋᴋᴋᴋᴋᴋᴋᴋᴋᴋᴋ', f'ꜪႽႽꜪ ∁𝝠𝑵𝝠Ŀ DO {canal_nome} Ꜫ ⋓ℳ ĿІ☓𝛐 ᵏᵏᵏᵏᵏᵏᵏᵏᵏᵏᵏᵏᵏᵏᵏᵏᵏᵏᵏᵏᵏᵏᵏᵏᵏ', f'ÊઽઽÊ 𝖢𝔸𝚴𝔸ւ Ḍ𝘰 {canal_nome} Ê ᙀΜ ւɪᕁ𝘰 ккккккккккккккккккккккккк', f'ㅌ𐒡𐒡ㅌ 𝙲𝚲𝐍𝚲ᒻ ḐѺ {canal_nome}  ㅌ ປന ᒻǀ𝙭Ѻ ҜҜҜҜҜҜҜҜҜҜҜҜҜҜҜҜҜҜҜҜҜҜҜҜҜ', f'OS VIDEOS DO {canal_nome} SAO UM LIXO KKKKKKKKKKKKKKKKKKKKKKK', f'θŜ ˅𝘐ÐЀθŜ Ðθ {canal_nome} ŜἈθ UM Ł𝘐𝛘θ 𝘬𝘬𝘬𝘬𝘬𝘬𝘬𝘬𝘬𝘬𝘬𝘬𝘬𝘬𝘬𝘬𝘬𝘬𝘬𝘬𝘬𝘬𝘬', f'ɵŠ 𝑉ꟾᗞꗋɵŠ ᗞɵ {canal_nome} Š𝝖ɵ ⋃ო ꜖ꟾӼɵ 𝙺𝙺𝙺𝙺𝙺𝙺𝙺𝙺𝙺𝙺𝙺𝙺𝙺𝙺𝙺𝙺𝙺𝙺𝙺𝙺𝙺𝙺𝙺', f'ØS VƗĐɆØS ĐØ {canal_nome} SȺØ ᵾM ŁƗXØ ꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀ', f'Ø₴ VłĐɆØ₴ ĐØ {canal_nome} ₴₳Ø Ʉ₥ ⱠłӾØ ₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭', f'Ō𝙎 ∇ǀⅮƩŌ𝙎 ⅮŌ {canal_nome} 𝙎ᴀŌ ∐ᗰ ᒻǀ𝘟Ō ҡҡҡҡҡҡҡҡҡҡҡҡҡҡҡҡҡҡҡҡҡҡҡ', f'MEU CANAL DA 10 A 0 NO CANAL DO {canal_nome} KKKKKKKKKKKKKK', f'ᙏ𝜠Մ ᴄ𝛬Ꞑ𝛬˪ 𝘋𝛬 𝞘𝙊 𝛬 𝙊 Ꞑ߀ ᴄ𝛬Ꞑ𝛬˪ 𝘋߀ ḳḳḳḳḳḳḳḳḳḳḳḳḳḳ', f'₥ɆɄ ₵₳₦₳Ⱡ Đ₳ 10 ₳ 0 ₦Ø ₵₳₦₳Ⱡ ĐØ ₭₭₭₭₭₭₭₭₭₭₭₭₭₭', f'๓ēน ¢คຖคl ໓ค 10 ค 0 ຖ໐ ¢คຖคl ໓໐ kkkkkkkkkkkkkk', f'MɆᵾ ȻȺNȺŁ ĐȺ 10 Ⱥ 0 NØ ȻȺNȺŁ ĐØ ꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀ', f'𝕄𝔼𝕌 ℂ𝔸ℕ𝔸𝕃 𝔻𝔸 𝟙𝟘 𝔸 𝟘 ℕ𝕆 ℂ𝔸ℕ𝔸𝕃 𝔻𝕆 𝕂𝕂𝕂𝕂𝕂𝕂𝕂𝕂𝕂𝕂𝕂𝕂𝕂𝕂', 'NAO SEI PORQUE TEM GENTE QUE VE ESSE LIXO DE CANAL KKKKKKKKKKKKKKKKKKKK', 'NȺØ SɆƗ ⱣØɌꝖᵾɆ ŦɆM ǤɆNŦɆ ꝖᵾɆ VɆ ɆSSɆ ŁƗXØ ĐɆ ȻȺNȺŁ ꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀ', '₦₳Ø ₴Ɇł ₱ØⱤQɄɆ ₮Ɇ₥ ₲Ɇ₦₮Ɇ QɄɆ VɆ Ɇ₴₴Ɇ ⱠłӾØ ĐɆ ₵₳₦₳Ⱡ ₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭', '𝙽𝙰𝙾 𝚂𝙴𝙸 𝙿𝙾𝚁𝚀𝚄𝙴 𝚃𝙴𝙼 𝙶𝙴𝙽𝚃𝙴 𝚀𝚄𝙴 𝚅𝙴 𝙴𝚂𝚂𝙴 𝙻𝙸𝚇𝙾 𝙳𝙴 𝙲𝙰𝙽𝙰𝙻 𝙺𝙺𝙺𝙺𝙺𝙺𝙺𝙺𝙺𝙺𝙺𝙺𝙺𝙺𝙺𝙺𝙺𝙺𝙺𝙺', 'Ň⋀𝝧 𝕊𝙴ߊ 𝚸𝝧ʀǪ𝑈𝙴 𝚃𝙴Ϻ 𝗚𝙴Ň𝚃𝙴 Ǫ𝑈𝙴 ⋁𝙴 𝙴𝕊𝕊𝙴 Ꝉߊẋ𝝧 𝓓𝙴 ᘓ⋀Ň⋀Ꝉ 𝘬𝘬𝘬𝘬𝘬𝘬𝘬𝘬𝘬𝘬𝘬𝘬𝘬𝘬𝘬𝘬𝘬𝘬𝘬𝘬', 'ɴÅ𝜪 𝕊𝐸∣ ᒆ𝜪𝓡ǫᕫ𝐸 〒𝐸𝕄 Ᏻ𝐸ɴ〒𝐸 ǫᕫ𝐸 Ɐ𝐸 𝐸𝕊𝕊𝐸 L∣𝕏𝜪 ᗫ𝐸 ᥴÅɴÅL 𝐾𝐾𝐾𝐾𝐾𝐾𝐾𝐾𝐾𝐾𝐾𝐾𝐾𝐾𝐾𝐾𝐾𝐾𝐾𝐾', f'Quem assiste o canal do {canal_nome} provalvemente foi estru pado na infancia KKKKKKKKKKKKKKKKKKKKKKKKKKK', f'𝘘𝞄𝚎ɱ ā𝓢𝓢Ĭ𝓢ŧ𝚎 Ө Ꮯāղā｜ 𝙙Ө {canal_nome} ƥ𝚛Ө𝘃ā｜𝘃𝚎ɱ𝚎ղŧ𝚎 𝚏ӨĬ 𝚎𝓢ŧ𝚛𝞄 ƥā𝙙Ө ղā Ĭղ𝚏āղᏟĬā κκκκκκκκκκκκκκκκκκκκκκκκκκκ', f'𝑸𝒖𝒆𝒎 𝒂𝒔𝒔𝒊𝒔𝒕𝒆 𝒐 𝒄𝒂𝒏𝒂𝒍 𝒅𝒐 {canal_nome} 𝒑𝒓𝒐𝒗𝒂𝒍𝒗𝒆𝒎𝒆𝒏𝒕𝒆 𝒇𝒐𝒊 𝒆𝒔𝒕𝒓𝒖 𝒑𝒂𝒅𝒐 𝒏𝒂 𝒊𝒏𝒇𝒂𝒏𝒄𝒊𝒂 𝑲𝑲𝑲𝑲𝑲𝑲𝑲𝑲𝑲𝑲𝑲𝑲𝑲𝑲𝑲𝑲𝑲𝑲𝑲𝑲𝑲𝑲𝑲𝑲𝑲𝑲𝑲', f'ꝖᵾɆM ȺSSƗSŦɆ Ø ȻȺNȺŁ ĐØ {canal_nome} ⱣɌØVȺVɆŁMɆNŦɆ FØƗ ɆSŦɌᵾ ⱣȺĐØ NȺ ƗNFȺNȻƗȺ ꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀ', f'QɄɆ₥ ₳₴₴ł₴₮Ɇ Ø ₵₳₦₳Ⱡ ĐØ {canal_nome} ₱ⱤØV₳VɆⱠ₥Ɇ₦₮Ɇ ₣Øł Ɇ₴₮ⱤɄ ₱₳ĐØ ₦₳ ł₦₣₳₦₵ł₳ ₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭', f'qυєм αѕѕιѕтє σ ¢αηαℓ ∂σ {canal_nome} ρяσνανєℓмєηтє ƒσι єѕтяυ ρα∂σ ηα ιηƒαη¢ια ккккккккккккккккккккккккккк', f'A maoiria dos fans do {canal_nome} deve ter sido molestado pelo tio na infancia KKKKKKKKKKKKKKKKKKKKKKKKK', f'₳ ₥₳łØⱤł₳ ĐØ₴ ₣₳₦₴ ĐØ {canal_nome} ₣Øł ₥ØⱠɆ₴₮₳ĐØ ₱ɆⱠØ ₮łØ ₦₳ ł₦₣₳₦₵ł₳ ₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭', f'Ⱥ MȺƗØɌƗȺ ĐØS FȺNS ĐØ {canal_nome} FØƗ MØŁɆSŦȺĐØ ⱣɆŁØ ŦƗØ NȺ ƗNFȺNȻƗȺ ꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀ', f'α мαισяια ∂σѕ ƒαηѕ ∂σ {canal_nome} ƒσι мσℓєѕтα∂σ ρєℓσ тισ ηα ιηƒαη¢ια ккккккккккккккккккккккккк', f'À 𝝡À𝘐𝜪𝗥𝘐À ᗟ𝜪S ₣ÀṆS ᗟ𝜪 {canal_nome} ₣𝜪𝘐 𝝡𝜪🇱ᇀS𝖳Àᗟ𝜪 𝜬ᇀ🇱𝜪 𝖳𝘐𝜪 ṆÀ 𝘐Ṇ₣ÀṆⲥ𝘐À ǨǨǨǨǨǨǨǨǨǨǨǨǨǨǨǨǨǨǨǨǨǨǨǨǨ', f'𝚨 Ϻ𝚨𝖨𝟶🇷𝖨𝚨 Ď𝟶ﮐ ғ𝚨ᶰﮐ Ď𝟶 {canal_nome} ғ𝟶𝖨 Ϻ𝟶Ḷ∈ﮐ𝐓𝚨Ď𝟶 Ṕ∈Ḷ𝟶 𝐓𝖨𝟶 ᶰ𝚨 𝖨ᶰғ𝚨ᶰⲤ𝖨𝚨 ҝҝҝҝҝҝҝҝҝҝҝҝҝҝҝҝҝҝҝҝҝҝҝҝҝ', 'Só tem gente que foi estru pado na infancia nesse canal KKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKKK', 'şó ŧ𝑒𝓶 𝒈𝑒ᥰŧ𝑒 𝗊𐌵𝑒 🝡σĺ 𝑒ડŧᵣ𐌵 ϸ𝝰ժσ ᥰ𝝰 ĺᥰ🝡𝝰ᥰϲĺ𝝰 ᥰ𝑒ડડ𝑒 ϲ𝝰ᥰ𝝰▎ кккккккккккккккккккккккккккккккккк', 'ѕó тєм gєηтє qυє ƒσι єѕтяυ ρα∂σ ηα ιηƒαη¢ια ηєѕѕє ¢αηαℓ кккккккккккккккккккккккккккккккккк', 'Só ŧɇm̷ ǥɇn̷ŧɇ ꝗᵾɇ føɨ ɇs̷ŧɍᵾ ᵽa̷đø n̷a̷ ɨn̷fa̷n̷ȼɨa̷ n̷ɇs̷s̷ɇ ȼa̷n̷a̷ł ꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀꝀ', '₴ó ₮Ɇ₥ ₲Ɇ₦₮Ɇ QɄɆ ₣Øł Ɇ₴₮ⱤɄ ₱₳ĐØ ₦₳ ł₦₣₳₦₵ł₳ ₦Ɇ₴₴Ɇ ₵₳₦₳Ⱡ ₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭₭', 'S̷ó̷ ̷t̷e̷m̷ ̷g̷e̷n̷t̷e̷ ̷q̷u̷e̷ ̷f̷o̷i̷ ̷e̷s̷t̷r̷u̷ ̷p̷a̷d̷o̷ ̷n̷a̷ ̷i̷n̷f̷a̷n̷c̷i̷a̷ ̷n̷e̷s̷s̷e̷ ̷c̷a̷n̷a̷l̷ ̷K̷K̷K̷K̷K̷K̷K̷K̷K̷K̷K̷K̷K̷K̷K̷K̷K̷K̷K̷K̷K̷K̷K̷K̷K̷K̷K̷K̷K̷K̷K̷K̷K̷K̷']
  request_body = {'snippet': {'parentId': id, 'textOriginal': random.choice(msgs)}}
  response = service.comments().insert(part='snippet', body=request_body).execute()
  cont += 1



def get_comment_threads(id):
  global commentid
  results = service.commentThreads().list(part="snippet", videoId=id, textFormat="plainText").execute()
  comment = results["items"][0]["snippet"]["topLevelComment"]
  likecount = comment["snippet"]["likeCount"] 
  commentid = comment["id"]
  if commentid in comentarios:
    pass
  else:
    comentarios.append(commentid)
    comentar(commentid)
  


def main():
  global cont
  try:
    time.sleep(1)
    for i in range(len(links_canal)):
      canal = Channel(links_canal[i])
      for url in canal.video_urls[:1]:
        global canal_nome
        canal_nome = canal.channel_name
        id_video = url.replace('https://www.youtube.com/watch?v=', '')
        current_time = time.strftime("%M")
        tempo_loop = int(current_time) + 5
        while True:
          if id_video in vistos:
            break
          else:
            if cont == 40:
              cont = 0
              break
            else:
              get_comment_threads(id_video)

              
        if id_video in vistos:
          pass
        else:
          vistos.append(id_video)
  except Exception:
    pass


                  


  
      



if __name__ == "__main__":

  app = FastAPI()
  print("oi)

  @app.get("/")
  async def root():
    return {"message": "Hello World"}

      
      
    
