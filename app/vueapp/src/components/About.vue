<template>
    <div>
        <div class="banner">
            <div class="header-container">
                <h1>About</h1>
            </div>
        </div>
        <div class="content">
            <div class="section">
                <p>I'm a self-taught web developer on Salt Spring Island, BC. I'm most experienced with Vue JS and Django. <br><br> 
                I enjoy making small web apps with Python or Javascript, have a look at my <router-link to="projects">projects</router-link> page to see what I've made.</p>
                <br>
            </div>
            <div class="hr"></div>
            <div class="section">
                <br>
                <p>What I'm currently working on:</p>
                <ul>
                    <li>Finishing up my personal website.</li>
                    <li>A cool little card reading app (progressive web app made with Vue JS Quasar framework.)</li>
                </ul>
            </div>

        </div>
        <vue-footer/>
    </div>
</template>

<script>
export default {
    components: {
        vueFooter: () => import("./Footer.vue"),
    },
};
</script>

<style lang="scss">
@import url("https://fonts.googleapis.com/css?family=Josefin+Slab|Ubuntu|Ubuntu+Condensed|Vollkorn|Lato");
$josefin: "Josefin Slab", serif;
$vollkorn: "Vollkorn", serif;
$ubuntu: "Ubuntu", sans-serif;
$ubuntucond: "Ubuntu Condensed", sans-serif;
$lato: "Lato", sans-serif;

.section {
  text-align: left;
}
.banner {
  background-color: $highlight2;
  height: 250px;
  max-width: $contentSize;
  margin: 30px auto;
  border-radius: 5px;
  display: flex;
  justify-content: left;
  align-items: center;
  //   background-image: url("../assets/webdevbanner.jpg");
  //   background-image: url("../assets/stocklaptop.jpg");
  // background-size: 1920px 1080px;
  // background-position-y: -250px;
  & .header-container {
    text-align: center;
    width: 70%;
    margin: auto;
    & h1 {
      font-family: $lato;
      color: $white;
      // text-shadow: 0px 0px 3px #000;
    }
  }
}

.content {
  margin: auto;
  max-width: $contentSize;
}
</style>
