## 토큰 (Token)

> 토큰(Token)은 말 그대로 동전이라는 뜻 이지만, 웹 상에서는 특정한 목적으로만 사용 가능한 동전에 일종의 권한.

### 웹 상에서의 토큰

서버에서는 사용자가 결제한 돈도 오고가서 권한이라는것이 중요하다. 인터넷에 사이트를 올리면 전 세계 사용자들이나 해커들이 접근 가능한데 사용자들의 돈을 보호하려면 본인만 접근 가능하도록 **본인 확인 수단**이 필요한데 그 수단으로 토큰을 이용한다.

### 토큰을 왜 사용할까?

- **Stateless**
    * 토큰 기반 인증은 서버에서 사용자의 정보를 가지지 않기 때문에 무상태성을 가져서 서바가 확장을 하여도 문제가 생기지 않게 된다.

- **모바일 어플리케이션에 적합하다**
    * Android나 iOS 모바일 어플리케이션을 개발할 때, 안전한 API를 만들기 위해서는 쿠키 컨테이너를 사용해야 하는 쿠키같은 인증시스템은 이상적이지 않다. 만약 토큰 기반 인증을 도입하면 더욱 간단하게 이 번거로움을 해결 할 수 있게 된다.

- **인증정보를 다른 어플리케이션으로 전달한다**
    * 대표적인 예제로 OAuth가 있다. 페이스북/구글 같은 소셜 계정들을 이용하여 다른 웹서비스에도 로그인 할 수 있게 한다.

- **보안**
    * 토큰 기반 인증 시스템을 사용하여 어플리케이션의 보안을 높일 수 있다.