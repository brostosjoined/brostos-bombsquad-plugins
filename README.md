# BombsquadRPC
[<img src="https://files.ballistica.net/ballistica_media/ballistica_logo_half.png" height="50">](https://github.com/efroemling/ballistica)[![pypresence](https://img.shields.io/badge/using-pypresence-00bb88.svg?style=for-the-badge&logo=discord&logoWidth=20)](https://github.com/qwertyquerty/pypresence)
[![PyPI version](https://img.shields.io/pypi/v/websocket_client)](https://pypi.org/project/websocket_client/)

A mod for the game  Bombsquad to display custom rich presence for mobile and desktop. Utilizes [`pypresence`](https://github.com/qwertyquerty/pypresence) and [`websocket-client`](https://github.com/websocket-client/websocket-client).
[Join official Discord Bombsquad Server](https://discord.gg/bombsquad-ballistica-official-1001896771347304639)

## 💀WARNING💀

```
Asking users to share a user token is forbidden by our Developer Policy and may result in action taken against your app and/or account. Please don't take that approach.
 
We may someday have other ways of setting presence on mobile, but for now it's really just the one method, which the game developers will need to pursue themselves if interested.
 
Thanks,
Shipwreck
``` 
```diff
- (ANDROID USERS)-> FROM NOW AND ONWARDS DOWNLOAD MODS THROUGH PLUGIN MANAGER AND OPEN SOURCED ONES
```

## Image samples
![Discord_vAOpR9SSxh](https://user-images.githubusercontent.com/67740566/231026276-b4d1c494-8e46-4325-ad25-54c69db5c19c.png)  ![ShareX_RcuOF8204k](https://user-images.githubusercontent.com/67740566/231027333-924bd5d2-876c-4fe7-b831-b449012eeac4.png)
![Discord_vjhHHSPjYL](https://user-images.githubusercontent.com/67740566/231523431-4f8bc8a3-bbb4-43b7-b3e4-b35c828f0d82.png)
![Discord_l10GSomMfm](https://user-images.githubusercontent.com/67740566/231523398-3df5d14f-1679-464a-bfdd-71ad85dd50d4.png)
![Discord_6K47DAcxqK](https://user-images.githubusercontent.com/67740566/231027292-e165fb77-409c-4ab3-bcba-75bff64a70e6.png)


## KizzyRPC
If you would like custom rpc for android I consider checking out [Kizzy](https://github.com/dead8309/Kizzy), a really great app.

[![](https://dcbadge.vercel.app/api/server/vUPc7zzpV5)](https://discord.gg/vUPc7zzpV5)

## Credits
- [Mr.Soomthy](https://github.com/imayushsaini)-Author of the new BCS modpack and server scripts and [Mikirog](https://github.com/TheMikirog) - Author of JRMP modpack
- [Dliwk](https://github.com/Dliwk)
- [Vaibhav](https://github.com/dead8309)


# UPNP/NAT-PMP
This plugin is used to autoport port 43210 to make bombsquad game joinable from the internet for upnp/nat-pmp ready router with upnp support from their ISP.
This code uses [nat-pmp client](https://github.com/jaraco/nat-pmp) and [upnpy](https://github.com/5kyc0d3r/upnpy).
The nat-pmp module is to support modern routers and apple devices while upnpy is a fallback for all routers that dont support natpmp.
