import ThirdPartyEmailPasswordReact from 'supertokens-auth-react/recipe/thirdpartyemailpassword'
import SessionReact from 'supertokens-auth-react/recipe/session'
import { appInfo } from './appInfo'

export const frontendConfig = () => {
  return {
    appInfo,
    recipeList: [
      ThirdPartyEmailPasswordReact.init({
        getRedirectionURL: async (context) => {
          if (context.action === "SUCCESS") {
              if (context.redirectToPath !== undefined) {
                  // we are navigating back to where the user was before they authenticated
                  return context.redirectToPath;
              }
              return "/posts/first-post";
          }
          return undefined;
        },
        signInAndUpFeature: {
          providers: [
            ThirdPartyEmailPasswordReact.Google.init(),
            // ThirdPartyEmailPasswordReact.Facebook.init(),
            // ThirdPartyEmailPasswordReact.Github.init(),
            // ThirdPartyEmailPasswordReact.Apple.init(),
          ],
        },
      }),
      SessionReact.init(),
    ],
  }
}