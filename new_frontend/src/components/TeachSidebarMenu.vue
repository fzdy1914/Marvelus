<template>
  <div class="sidebar-menu">
    <div class="nav-code">{{course.code}}</div>
    <div class="nav-title">{{course.title}}</div>
    <div class="nav-info">{{course.info}}</div>
    <div class="nav-row">Role: <b>Prof</b></div>
    <div class="p-menu p-component">
      <ul class="p-menu-list p-reset">
        <li class="p-menuitem" :class="{ active: isInfoActive }" @click="goInfo()">
          <a class="p-menuitem-link">Course Info</a>
        </li>
        <li class="p-menuitem" :class="{ active: isStudentActive }" @click="goStudent()">
          <a class="p-menuitem-link">Students</a>
        </li>
        <li class="p-menuitem" :class="{ active: isRequestsActive }" @click="goRequests()">
          <a class="p-menuitem-link">Requests</a>
        </li>
        <li class="p-menuitem" :class="{ active: isTAsActive }" @click="goTAs()">
          <a class="p-menuitem-link">TAs</a>
        </li>
        <li class="p-menuitem" :class="{ active: isTutActive }" @click="goTuts()">
          <a class="p-menuitem-link">Tutorials</a>
        </li>
        <li class="p-menuitem" :class="{ active: isForumActive }" @click="goForum()">
          <a class="p-menuitem-link">Forum</a>
        </li>
      </ul>
    </div>
  </div>
</template>

<script>
export default {
  name: "TeachSideBarMenu",
  data(){
    return{
      course: {},
    }
  },
  computed: {
    isInfoActive: function () {
      return this.$route.name == 'TeachDetail' || this.$route.name == 'TeachDetailInfo'
    },
    isTutActive: function () {
      return this.$route.name == 'TeachDetailTutList' || this.$route.name == 'TeachDetailTutDetail'
    },
    isStudentActive: function () {
      return this.$route.name == 'TeachDetailStudent'
    },
    isRequestsActive: function () {
      return this.$route.name == 'TeachDetailRequests'
    },
    isTAsActive: function () {
      return this.$route.name == 'TeachDetailTAs'
    },
    isForumActive: function () {
      return this.$route.name.indexOf('Forum') >= 0 || this.$route.name.indexOf('Post') >= 0
    },
  },
  mounted(){
    this.getCourse();
  },
  methods: {
    getCourse: function () {
      this.$axios.request({
        url: this.$url + 'course/code/' + this.$route.params.code + '/',
        method: 'GET'
      }).then(response => {
        let data = response.data
        if (data.state === true) {
          this.course = data.data.course
        } else {
          this.state = false
          this.msg = data.error
        }
      })
    },
    goInfo: function () {
      if (this.$route.name != 'TeachDetailInfo') {
        this.$router.push({name: 'TeachDetailInfo', params: {code: this.$route.params.code}})
      }
    },
    goTuts: function () {
      if (this.$route.name != 'TeachDetailTutList') {
        this.$router.push({name: 'TeachDetailTutList', params: {code: this.$route.params.code}})
      }
    },
    goStudent: function () {
      if (this.$route.name != 'TeachDetailStudent') {
        this.$router.push({name: 'TeachDetailStudent', params: {code: this.$route.params.code}})
      }
    },
    goRequests: function () {
      if (this.$route.name != 'TeachDetailRequests') {
        this.$router.push({name: 'TeachDetailRequests', params: {code: this.$route.params.code}})
      }
    },
    goTAs: function () {
      if (this.$route.name != 'TeachDetailTAs') {
        this.$router.push({name: 'TeachDetailTAs', params: {code: this.$route.params.code}})
      }
    },
    goForum: function () {
      if (this.$route.name != 'TeachDetailForumList') {
        this.$router.push({name: 'TeachDetailForumList', params: {code: this.$route.params.code}})
      }
    },
  }
}
</script>

<style scoped>
.sidebar-menu {
  display: inline-block;
  float: left;
}
.nav-code{
  color: #1976d2;
  max-width: 150px;
  margin-bottom: 15px;
  font-weight: bold;
  font-size: 17px;
  margin-left: 12.5px;
}
.nav-title{
  max-width: 150px;
  font-weight: Bold ;
  font-size: 20px;
  margin-bottom: 15px;
  margin-left: 12.5px;
}
.nav-info{
  max-width: 150px;
  margin-bottom: 15px;
  margin-left: 12.5px;
}
.nav-row {
  font-size: 16px;
  max-width: 150px;
  margin-bottom: 15px;
  margin-left: 12.5px;
  color: #5e5e5e;
}
.active {
  background-color: #dedede;
  font-size:15px;
  font-weight: bold;
}
</style>