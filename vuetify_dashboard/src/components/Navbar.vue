<template>
    <nav>
        <v-app-bar color="red" dark app>
                <v-app-bar-nav-icon>

                </v-app-bar-nav-icon>
                <v-toolbar-title class="text-uppercase">
                    <span class="font-weight-light">Nurullo </span>
                    <span>Budget</span>
                </v-toolbar-title>
                <v-spacer></v-spacer>
                <!-- <menu offset-y>
                    <template slot:activator="{on}">
                        <v-btn text v-on="on">
                            <v-icon left>expand_more</v-icon>
                            <span>Menu</span>
                        </v-btn>
                    </template>
                    <v-list flat>
                        <v-list-item v-for="link in links" :key="link.text" router :to="link.route">
                            <v-list-item-title>{{ link.text }}</v-list-item-title>
                        </v-list-item>
                    </v-list>
                </menu> -->
                <v-btn text>
                    <span>Exit</span>
                    <v-icon right> exit_to_app</v-icon>
                </v-btn>

        </v-app-bar>
    </nav>
</template>

<script>
export default {
    name: "Navbar",
    data: () => {
        drawer: true
        links: [
            {'icon': 'dashboard', text: 'Dashboard', route: '/'},
            {'icon': 'folder', text: 'My Project', route: '/projects'},
            {'icon': 'person', text: 'Team', route: '/team'},
        ]
    }
}
</script>
