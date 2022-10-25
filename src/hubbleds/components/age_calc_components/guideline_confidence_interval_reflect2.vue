<template>
  <scaffold-alert
    header-text="Identify Your Confidence Interval"
    @back="
      state.marker = 'age_dis1';
    "
    @next="
      state.marker = 'age_uni1c';
    "
  >
    <div
      class="mb-4"
    >
      <p>
        Based on these results from your class, what do you think is the <strong>most likely value</strong> of the age of the universe and what is a <strong>likely range</strong> of possible values?
      </p>
      <v-row>
        <v-col
          cols="10"
          offset="1"
        >
          1. My best guess for the age of the universe based on my entire class’s data set: 
        </v-col>
      </v-row>
      <v-row>
        <v-col
          cols="12"
          lg="4"
        >
          <free-response
            outlined
            auto-grow
            rows="1"
            label="Best Guess Age"
            tag="best-guess-age"
            suffix="Gyr"
          ></free-response>
        </v-col>
        <v-spacer></v-spacer>
        <v-col
          cols="12"
          lg="4"
        >
          <v-btn
            color="secondary lighten-1"
            depressed
            outlined
            elevation="0"
            @click="hint1_dialog = true"
          >
            hint
            <v-dialog
              v-model="hint1_dialog"
              persistent
              max-width="600px"
            >
              <v-card
                class="mx-auto"
              >
                <v-toolbar
                  color="secondary"
                  dense
                  dark
                >
                  <v-toolbar-title
                    class="text-h6 text-uppercase font-weight-regular"
                  >
                    Hint #1
                  </v-toolbar-title>
                  <v-spacer></v-spacer>
                  <span
                    @click="
                      () => {
                        $emit('close');
                        hint1_dialog = false;
                      }
                    "
                  >
                    <v-btn
                      icon
                    >
                      <v-icon>mdi-close</v-icon>
                    </v-btn>
                  </span>
                </v-toolbar>
                <div
                  class="pa-6"
                >
                  A gold standard in scientific practice is reproducibility. If someone else performs a procedure you did and obtains the same or very similar result, that means your result was reproducible and is therefore more plausible.
                </div>
              </v-card>
            </v-dialog>
          </v-btn>
          <v-btn
            v-if="confint_step == 1"
            class="black--text"
            color="accent"
            elevation="0"
            @click="() => { confint_step = confint_step + 1; }"
          >
            next
          </v-btn>
        </v-col>
      </v-row>

      <v-row>
        <v-col
          cols="12"
          lg="9"
        >
          2. My best guess for the likely range of ages of the universe based on my entire class’s data set: 
        </v-col>
        <v-col>
          <v-btn
            color="secondary lighten-1"
            @click="hint2_dialog=true"
          >
            hint
            <v-dialog
              v-model="hint2_dialog"
              persistent
              max-width="600px">
              <v-card
                class="mx-auto"
              >
                <v-toolbar
                  color="secondary"
                  dense
                  dark
                >
                  <v-toolbar-title
                    class="text-h6 text-uppercase font-weight-regular"
                  >
                    Hint #2
                  </v-toolbar-title>
                  <v-spacer></v-spacer>
                  <span
                    @click="
                      () => {
                        $emit('close');
                        hint2_dialog = false;
                      }
                    "
                  >
                    <v-btn icon>
                      <v-icon>mdi-close</v-icon>
                    </v-btn>
                  </span>
                </v-toolbar>
                <div class="pa-6">
                  <p>
                    The range you pick will have a tradeoff between how likely it is that the “true” value actually lies within the range you choose vs. having a narrow enough range that your measurement is actually useful. A very large range is more likely to include the "true" value, but may be so nonspecific that it is not useful. A narrow range has more specificity but may not include the "true" value.
                  </p>
                  <p>
                    Different people will feel more or less comfortable with the different sides of this tradeoff, and there isn’t really a right or wrong answer as long as you justify why you
                    chose what you did.
                  </p>
                  <p>
                    If you are feeling really stuck, feel free to discuss this with a classmate or your instructor.
                  </p>
                </div>
              </v-card>
            </v-dialog>
          </v-btn>
        </v-col>
      </v-row>
      <v-row>
        <v-col
          cols="12"
          lg="3"
        >
          <free-response
            outlined
            auto-grow
            rows="1"
            label="Likely Low Age"
            tag="likely-low-age"
          ></free-response>
        </v-col>
        <v-col
          lg="2"
        >
          Gyr
        </v-col>
        <v-col
          cols="12"
          lg="3"
        >
          <free-response
            outlined
            auto-grow
            rows="1"
            label="Likely High Age"
            tag="likely-high-age"
          ></free-response>
        </v-col>
        <v-col
          lg="2"
        >
          Gyr
        </v-col>
      </v-row>

      <p class="mt-4">
        3. Explain why you chose your values using information from the scatterplot and/or the histogram:
      </p>
      <free-response
        outlined
        auto-grow
        rows="2"
        label="My Reasoning"
        tag="my-reasoning"
      ></free-response>

      <v-row>
        <v-col
          cols="12"
          lg="9"
        >
        4. Describe how confident you feel in your reported age and high/low values:
        </v-col>
        <v-col>
          <v-btn
            color="secondary lighten-1"
            @click="hint3_dialog=true"
          >
            hint
            <v-dialog
              v-model="hint3_dialog"
              persistent
              max-width="600px"
            >
              <v-card
                class="mx-auto"
              >
                <v-toolbar
                  color="secondary"
                  dense
                  dark
                >
                  <v-toolbar-title
                    class="text-h6 text-uppercase font-weight-regular"
                  >
                    Hint #3
                  </v-toolbar-title>
                  <v-spacer></v-spacer>
                  <span
                    @click="
                      () => {
                        $emit('close');
                        hint3_dialog = false;
                      }
                    "
                  >
                    <v-btn
                      icon
                    >
                      <v-icon>mdi-close</v-icon>
                    </v-btn>
                  </span>
                </v-toolbar>
                <div class="pa-6">
                  <p>
                    The way scientists think about their reported range of a measurement is to imagine the likelihood that the “true” value lies within the specified range. For example, you might give a narrower range of possible values, where you believe the true value has a 2 in 3 chance of being within the specified range. Or you might give a wider range of possible values, where you believe the true value has a 19 in 20 chance of being within the specified range.
                  </p>
                  <p>
                    You can do this by counting how many of your classmates’ measurements fall within the range you selected vs how many measurements were made all together within your class.
                  </p>
                </div>
              </v-card>
            </v-dialog>
          </v-btn>
        </v-col>
      </v-row>

      <free-response
        outlined
        auto-grow
        rows="2"
        label="My Level of Confidence"
        tag="my-confidence"
      ></free-response>
    </div>
  </scaffold-alert>
</template>
