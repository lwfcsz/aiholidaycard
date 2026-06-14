from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, HTMLResponse
from pydantic import BaseModel
import uuid
import random
from datetime import datetime
import os

app = FastAPI(title="AI节日贺卡生成API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

cards_db = {}

BLESSING_TEMPLATES = {
    "birthday": {
        "warm": [
            "🎂 生日快乐！愿你的每一天都像生日蛋糕一样甜蜜，愿你的梦想像蜡烛一样照亮前行的路途！",
            "🎉 在这特别的日子里，祝你生日快乐！愿你永远保持童心，永远幸福安康！",
            "🎈 生辰吉乐，福寿安康。愿新的一岁，所有美好如期而至！"
        ],
        "humorous": [
            "🎂 又老了一岁！不过没关系，反正颜值还是在线的！生日快乐，继续嗨！",
            "🎉 恭喜你解锁新的一岁！愿你的发际线稳如泰山，生日快乐！",
            "🎈 生日年年有，今年特别牛！生日快乐，做个快乐的干饭人！"
        ],
        "elegant": [
            "🎂 良辰吉日，福寿安康。愿君岁岁常欢愉，年年皆胜意。",
            "🎉 华诞欣逢盛世开，好风佳月尽袭来。祝君生日快乐，万事顺遂。",
            "🎈 生如夏花之绚烂，岁月静好。愿你所愿皆可得，所爱皆相守。"
        ]
    },
    "festival": {
        "warm": [
            "🏮 新春快乐！愿新的一年，平安喜乐，万事胜意！🎊",
            "🎄 圣诞快乐！愿这个冬天，有人问你粥可温，有人与你立黄昏。",
            "🎃 万圣节快乐！愿你的人生充满惊喜和欢乐！"
        ],
        "humorous": [
            "🏮 过年啦！恭喜发财，红包拿来！🎁 新春快乐！",
            "🎄 圣诞节到啦！希望你的袜子装满礼物，希望你的肚子装满美食！",
            "🎃 万圣节不给糖就捣蛋！祝你有个甜甜的节日！"
        ],
        "elegant": [
            "🏮 春回大地，万物复苏。恭贺新禧，福满人间。",
            "🎄 银装素裹，圣诞祥和。愿你心有所属，岁岁平安。",
            "🏮 爆竹声中一岁除，春风送暖入屠苏。新年快乐！"
        ]
    },
    "graduation": {
        "warm": [
            "🎓 毕业快乐！愿你前程似锦，归来仍是少年！",
            "🎓 恭喜毕业！这是终点，也是起点。未来的路，勇敢去闯吧！",
            "🎓 毕业不是结束，而是新旅程的开始。加油，未来的你！"
        ],
        "humorous": [
            "🎓 终于毕业了！再也不用担心挂科了！毕业快乐！🎉",
            "🎓 恭喜解锁'社会大学'入学资格！愿你学业有成！😂",
            "🎓 毕业啦！再也不用听室友打呼噜了！前程似锦！"
        ],
        "elegant": [
            "🎓 鹏程万里，前途似海。愿你以梦为马，不负韶华。",
            "🎓 天高任鸟飞，海阔凭鱼跃。愿此去繁花似锦，再见依然如故。",
            "🎓 长风破浪会有时，直挂云帆济沧海。毕业快乐！"
        ]
    },
    "blessing": {
        "warm": [
            "🌸 愿你被世界温柔以待，愿你所遇皆美好。",
            "🌸 祝你开心每一天，幸福永相伴！",
            "🌸 愿你的生活如诗如画，每一天都充满阳光！"
        ],
        "humorous": [
            "🌸 祝你钱包鼓鼓，身体棒棒，吃嘛嘛香！😄",
            "🌸 愿你睡觉睡到自然醒，数钱数到手抽筋！",
            "🌸 祝你心想事成，万事如意，笑口常开！😂"
        ],
        "elegant": [
            "🌸 静水流深，沧笙踏歌。愿你岁月无恙，一切安好。",
            "🌸 时光清浅，岁月嫣然。愿你所见皆温柔，所遇皆良人。",
            "🌸 愿你三冬暖，愿你春不寒。愿你一路上，有良人相伴。"
        ]
    }
}

CARD_TEMPLATES = {
    "warm": {"name": "温暖风格", "background": "linear-gradient(135deg, #f093fb 0%, #f5576c 100%)"},
    "humorous": {"name": "幽默风格", "background": "linear-gradient(135deg, #fa709a 0%, #fee140 100%)"},
    "elegant": {"name": "优雅风格", "background": "linear-gradient(135deg, #4facfe 0%, #00f2fe 100%)"}
}

class GenerateRequest(BaseModel):
    occasion: str
    style: str
    recipient: str = ""
    custom_words: str = ""

@app.get("/")
async def root():
    frontend_path = os.path.join(os.path.dirname(__file__), "..", "frontend", "index.html")
    return FileResponse(frontend_path)

@app.get("/api/templates")
async def get_templates():
    return {"success": True, "data": CARD_TEMPLATES}

@app.post("/api/generate")
async def generate_card(request: GenerateRequest):
    templates = BLESSING_TEMPLATES.get(request.occasion, {}).get(request.style, [])
    if not templates:
        raise HTTPException(status_code=400, detail="Invalid occasion or style")
    
    blessing = random.choice(templates)
    if request.custom_words:
        blessing = f"{blessing}\n\n💬 {request.custom_words}"
    if request.recipient:
        blessing = f"致 {request.recipient}：\n\n{blessing}"
    
    card_id = str(uuid.uuid4())[:8]
    
    card_data = {
        "id": card_id,
        "occasion": request.occasion,
        "style": request.style,
        "recipient": request.recipient,
        "blessing": blessing,
        "created_at": datetime.now().isoformat(),
        "template": CARD_TEMPLATES.get(request.style, CARD_TEMPLATES["warm"])
    }
    cards_db[card_id] = card_data
    
    return {
        "success": True,
        "data": {
            "card_id": card_id,
            "blessing": blessing,
            "template": card_data["template"],
            "share_url": f"/card/{card_id}"
        }
    }

@app.get("/api/card/{card_id}")
async def get_card(card_id: str):
    card = cards_db.get(card_id)
    if not card:
        raise HTTPException(status_code=404, detail="Card not found")
    return {"success": True, "data": card}

@app.get("/card/{card_id}")
async def view_card(card_id: str):
    card = cards_db.get(card_id)
    if not card:
        return {"error": "贺卡不存在"}
    
    occasion_emojis = {"birthday": "🎂", "festival": "🏮", "graduation": "🎓", "blessing": "🌸"}
    occasion_names = {"birthday": "生日快乐", "festival": "节日快乐", "graduation": "毕业快乐", "blessing": "祝福"}
    
    emoji = occasion_emojis.get(card['occasion'], "🎊")
    name = occasion_names.get(card['occasion'], "贺卡")
    date_str = datetime.fromisoformat(card['created_at']).strftime('%Y年%m月%d日')
    
    html_content = f"""
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>AI贺卡 - {card['occasion']}</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        body {{
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            padding: 20px;
        }}
        .card {{
            max-width: 500px;
            width: 100%;
            padding: 40px;
            border-radius: 20px;
            box-shadow: 0 20px 60px rgba(0,0,0,0.3);
            text-align: center;
        }}
    </style>
</head>
<body>
    <div class="card" style="background: {card['template']['background']}">
        <div class="text-6xl mb-4">{emoji}</div>
        <h1 class="text-2xl font-bold text-white mb-4">{name}</h1>
        <p class="text-white/90 text-lg whitespace-pre-line leading-relaxed">{card['blessing']}</p>
        <p class="text-white/60 text-sm mt-4">{date_str}</p>
    </div>
</body>
</html>
"""
    return HTMLResponse(content=html_content, media_type="text/html")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)