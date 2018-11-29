
Vue.component('search-result', {

	props: ['store','image','url','title','price'],

	template: `
			<div class="col-lg-4 col-md-4 mb-3 slideout-item scaleup" v-touch:swipe.right="onSwipeLeft">
            <div :class="store" class="card card-border-color">
                <div class="card-body">
                  <div class="row">
                  <div class="col-md-5 col-5 col-sm-5 col-xs-5">
                    <div class="align-middle mtb-auto"><a :href="url"><img class="img-fluid" :src="image" style="width:120px;"></a></div>
                  </div>
                  <div class="col-md-7 col-7 col-sm-7 col-xs-7">
                    <a :href="url" class="cl1"><p><strong v-text=title></strong></p></a>
                    <p>₦{{ price }}</p>
                    <button @click="showProduct" data-toggle="modal" data-target="#myModal" :class="'bg-'+ store" class="btn btn-primary btn-block" style="margin-bottom:4px;white-space: normal;"> Buy from {{ store }}</button>
                  </div>
                </div>
                </div>
              </div>
          	</div>
    `,
    methods: {
    
            showProduct() {
              this.$emit('clicked', {'url':this.url, 'store':this.store});
            },
            onSwipeLeft() {
              this.$emit('removed');
            }
    }
});

Vue.component('lazy-load', {

	props: [],

	template: `
			<div class="col-lg-4 col-md-4 mb-3">
            <div class="lazy-div">
                  <div class="row">
                  <div class="col-md-5 col-5 col-sm-5 col-xs-5 animated-background">
                    
                  </div>
                  <div class="col-md-7 col-7 col-sm-7 col-xs-7">
                    <div class="animated-text lazy-text"></div>
                    <div class="animated-text lazy-text"></div>
                    <div class="animated-text lazy-text"></div>
                    <div class="animated-text lazy-text"></div>
                  </div>
                </div>
              </div>
            </div>
    `

});


var app = new Vue({

			el: '#root',
			data: {

				term : "",
				results: [],
				loading: false,
        productUrl: "",

				
			},

			computed: {
				searchResults() {
					return this.results.sort((a,b)=>parseFloat(a.price) - parseFloat(b.price));
				}
				
			},

			methods : {

				getResults() {
					this.loading = true;
					axios.get('/search/' + this.term).then(response => {this.loading = false; return this.results = response.data;}).catch(error => { this.loading = false; return console.log(error);});
				},

        setUrl(args) {
                this.productUrl = 'https://onlinestorecompare.herokuapp.com/product?url=' + args.url + '&store=' + args.store;
            },
        deleteElement(index) {
                this.results.splice(index, 1);;
            }
			}

		});