
def response_without_prefix(s, prefix="AI: "):
   s = s.replace("titaniic", "titanic")
   return s[len(prefix):] if s.startswith(prefix) else s